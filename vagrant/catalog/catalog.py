from flask import Flask, render_template

# Imports for CRUD operations on database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

app = Flask(__name__)
app.debug = True
app.secret_key = """M}XUZoTl+U3]j`Gk&d5ysi5)}GTIDA?9"""

# Create session and connect to the database
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/catalog/')
def showCatalog():
    '''This is the homepage which will show all current categories along with
    the latest added items. After logging in, a user has the ability to add,
    update or delete item info.'''
    categories = session.query(Category).all()
    latest_items = {'India Pale Ale (IPA)': 'Three Floyds BrooDoo',
            'Belgian Ale': 'Orval',
            'Belgian Strong Ale': 'Westvleteren Extra 8'}
    return render_template('catalog.html', categories=categories, latest_items=latest_items)


@app.route('/catalog.json')
def showCatalogJSON():
    # TODO: implement
    return "This is the JSON endpoint provided by the application."


@app.route('/catalog/<category>/')
@app.route('/catalog/<category>/items/')
def showCategory(category):
    ''' When a specific category has been selected, this page will show all
    the items available for that category.'''
    items = [char for char in category] # just for testing
    # TODO: imlement with items from DB
    return render_template('category.html', category=category, items=items)


@app.route('/catalog/<category>/<item>/')
def showItem(category, item):
    ''' When a specific item has been selected, this page will show all
    information of that item. After logging in, a user has the ability to
    select an item to update or delete its item info.'''
    return render_template('item.html', category=category, item=item)


@app.route('/catalog/items/new/')
def newItem():
    '''After logging in, this page gives the user the ability to add an item
    with item info.'''
    return render_template('item_new.html')


@app.route('/catalog/<item>/edit/')
def editItem(item):
    '''After logging in, this page gives the user the ability to update the item info.'''
    return render_template('item_edit.html', item=item)


@app.route('/catalog/<item>/delete/')
def deleteItem(item):
    '''After logging in, this page gives the user the ability to delete the
    item info.'''
    return render_template('item_delete.html', item=item)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
