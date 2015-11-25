from functools import wraps
from flask import Flask
from flask import make_response
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
from flask import url_for
from flask import flash
from flask import session

# Imports for CRUD operations on database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

# New imports for step to create anti forgery state token
import json
import random
import string

# Needed to handle the code sent back from the callback method
import httplib2
# flow_from_clientsecrets creates a flow object from client_secrets.json file
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

import requests

# Credentials for Google OAuth
GOOGLE_CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Beer Catalog"


app = Flask(__name__)
app.debug = True
app.secret_key = """M}XUZoTl+U3]j`Gk&d5ysi5)}GTIDA?9"""

# Create session and connect to the database
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db = DBSession()


# Decorator for required logins
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('You are not authorized, because you are not logged in.')
            return redirect(url_for('showCatalog', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


# Method to do the login, for now only with support for Google Plus
@app.route('/connect', methods=['POST'])
def connect():
    '''Exchange the one-time authorization token for a token and store
    the token in the session.'''

    # First confirm that the token that the client sends to server
    # matches the token that the server sent to the client, to validate
    # that the user is making the request.
    if request.args.get('state') != session['state']:
        # No further authentication will occur on the server side if
        # there is a mismatch between these state tokens
        response = make_response(json.dumps('Invalid state parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Proceed and collect the one-time authorization code from the server
    auth_code = request.data

    try:
        # Try to exchange this authorization code for a credentials
        # object, which will contain the access code for my server.
        # First create an OAuth Flow object and specify postmessage as
        # the one-time code flow.
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        # Initiate the exchange, passing in the one-time authorization
        # code as input, which results in a credentials object.
        credentials = oauth_flow.step2_exchange(auth_code)
    except FlowExchangeError:
        # In case of an error, send the response as a JSON-object.
        response = make_response(json.dumps(
            'Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check for a valid (working) access token inside of the credentials
    # object.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, it's invalid, so
    # abort. Send the response as a JSON-object.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # We now have a working access token. Now let's make sure we have
    # the right access token, by verifying that the access token is used
    # for the intended user.
    gplus_id = credentials.id_token['sub']
    # If the id of the token in the credentials object does not match
    # the id returned by the Google API server, we do not have the right
    # token. In that case send the error in a response as a JSON-object.
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != GOOGLE_CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    # Lastly, check if user is already logged in. In this case return a
    # 200 (successful authentication) without resetting all of the
    # login-session variables again.
    stored_credentials = session.get('credentials')
    stored_gplus_id = session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Assuming none of the if-statements for the checks were true, we
    # now have a valid access token, and the user is successfully able
    # to log in to the server. We should store the access token in the
    # user's login-session for later use.
    session['access_token'] = credentials.access_token
    session['gplus_id'] = gplus_id
    response = make_response(json.dumps('Successfully connected user'), 200)

    # Use the Google Plus API to get some more info about the user.
    # Send off a message with the access token, requesting the user info
    # allowed by the token-scope, and store it in an object (data).
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = json.loads(answer.text)
    # If successful, this method returns a response body with the
    # following structure (or something quite similar):
    # {
    #     "gender": string,
    #     "name": string,
    #     "given_name": string,
    #     "family_name": string,
    #     "id": string,
    #     "link": string,
    #     "picture": string,
    #     "email": string,
    #     "verified_email": bool,
    #     "hd": string
    # }
    # Now 'data' should have all these values filled in so long as the
    # user has specified them in their account.
    # Store the values we're interested in and add the provider to login
    # session:
    session['username'] = data['name']
    session['given_name'] = data['given_name']
    session['family_name'] = data['family_name']
    session['picture'] = data['picture']
    session['email'] = data['email']
    session['provider'] = 'google'

    # Check for existing user with this email address (or make a new one
    # if it doesn't exist yet) and get its User object.
    user_id = getUserID(session['email']) or createUser(session)
    session['user_id'] = user_id
    user = getUserInfo(session['user_id'])

    flash("You are now logged in as %s" % session['username'])
    return response


# Disconnect - Revoke a user's token and resset their session
@app.route("/disconnect")
@login_required
def disconnect():
    # Only disconnect a connected user.
    access_token = session.get('access_token')
    if access_token is None:
        # If there is no access_token, there's noone to disconnect from the app
        response = make_response(
            json.dumps('Current user is not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Execute HTTP GET request to revoke current token.
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        # Reset the user's session.
        del session['access_token']
        del session['gplus_id']
        del session['username']
        del session['given_name']
        del session['family_name']
        del session['email']
        del session['picture']
        del session['user_id']
        del session['provider']

        flash('You have been successfully logged out.')
        return redirect(url_for('showCatalog'))
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


def createUser(session):
    newUser = User(
        username=session['username'],
        given_name=session['given_name'],
        family_name=session['family_name'],
        email=session['email'],
        picture=session['picture']
    )
    db.add(newUser)
    flash('Added new user.')
    db.commit()
    user = db.query(User).filter_by(email=session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = db.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = db.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


@app.route('/')
@app.route('/catalog/')
def showCatalog():
    '''This is the homepage which will show all current categories along with
    the latest added items. After logging in, a user has the ability to add,
    update or delete item info.'''
    # Create a state token to prevent request forgery and store it in
    # the session for later validation.
    state = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for x in xrange(32))
    session['state'] = state
    categories = db.query(Category).all()

    latest_items = db.query(Item).order_by('-Item.id').limit(10)
    if 'user_id' not in session:
        return render_template('pub_catalog.html',
                               categories=categories,
                               latest_items=latest_items)
    else:
        return render_template('catalog.html',
                               categories=categories,
                               latest_items=latest_items)


@app.route('/catalog.json')
def showCatalogJSON():
    categories = db.query(Category).all()
    return jsonify(categories=[c.serialize for c in categories])


@app.route('/catalog/<int:category_id>/')
@app.route('/catalog/<int:category_id>/items/')
def showCategory(category_id):
    ''' When a specific category has been selected, this page will show all
    the items available for that category.'''
    current_category = db.query(Category).filter_by(id=category_id).one()
    categories = db.query(Category).all()
    items = db.query(Item).filter_by(
        category_id=category_id).order_by('Item.name')
    return render_template('category.html', categories=categories,
                           category=current_category, items=items)


@app.route('/catalog/<int:category_id>/<int:item_id>/')
def showItem(category_id, item_id):
    ''' When a specific item has been selected, this page will show all
    information of that item. After logging in, a user has the ability to
    select an item to update or delete its item info.'''
    category = db.query(Category).filter_by(id=category_id).one()
    item = db.query(Item).filter_by(id=item_id).one()
    if 'user_id' not in session:
        return render_template('pub_item.html', category=category, item=item)
    else:
        return render_template('item.html', category=category, item=item)


@app.route('/catalog/items/new/', methods=['GET', 'POST'])
@login_required
def newItem():
    '''After logging in, this page gives the user the ability to add an item
    with item info.'''
    categories = db.query(Category).all()

    if request.method == 'POST':
        newItem = Item(
            name=request.form['name'],
            category_id=request.form['category_id'],
            description=request.form['description'],
            user_id=session['user_id']
        )

        db.add(newItem)
        newItemCategory = db.query(Category).filter_by(
            id=newItem.category_id).one()
        flash((
            u'New beer "{}" has been successfully added to the category "{}". '
            u'Cheers!'.format(newItem.name, newItemCategory.name)
            ))
        db.commit()

        return redirect(url_for('showCatalog'))

    else:
        return render_template('item_new.html', categories=categories)


@app.route('/catalog/<item_id>/edit/', methods=['GET', 'POST'])
@login_required
def editItem(item_id):
    '''After logging in, this page gives the user the ability to update the
    item info.'''
    categories = db.query(Category).all()
    item = db.query(Item).filter_by(id=item_id).one()

    if session['user_id'] != item.user_id:
        response = make_response(json.dumps('Unauthorized'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    if request.method == 'POST':
        item.name = request.form['name']
        item.category_id = request.form['category_id']
        item.description = request.form['description']

        db.add(item)
        flash('Item has been modified')
        db.commit()

        return redirect(url_for('showCatalog'))

    else:
        return render_template('item_edit.html',
                               categories=categories, item=item)


@app.route('/catalog/<int:item_id>/delete/', methods=['GET', 'POST'])
@login_required
def deleteItem(item_id):
    '''After logging in, this page gives the user the ability to delete the
    item info.'''
    item = db.query(Item).filter_by(id=item_id).one()

    if session['user_id'] != item.user_id:
        response = make_response(json.dumps('Unauthorized'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    if request.method == 'POST':
        db.delete(item)
        flash('Deleted "%s" from the database.' % item.name)
        db.commit()
        return redirect(url_for('showCatalog'))
    else:
        return render_template('item_delete.html', item=item)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
