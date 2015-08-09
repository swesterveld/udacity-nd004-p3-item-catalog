from flask import Flask, render_template, request, redirect, jsonify, url_for

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
    latest_items = session.query(Item).limit(3)
    return render_template('catalog.html', categories=categories, latest_items=latest_items)


@app.route('/catalog.json')
def showCatalogJSON():
    categories = session.query(Category).all()
    return jsonify(categories= [c.serialize for c in categories])


@app.route('/catalog/<int:category_id>/')
@app.route('/catalog/<int:category_id>/items/')
def showCategory(category_id):
    ''' When a specific category has been selected, this page will show all
    the items available for that category.'''
    current_category = session.query(Category).filter_by(id=category_id).one()
    categories = session.query(Category).all()
    items = session.query(Item).filter_by(category_id=category_id).limit(3)
    return render_template('category.html', categories=categories,
            category=current_category, items=items)


@app.route('/catalog/<int:category_id>/<int:item_id>/')
def showItem(category_id, item_id):
    ''' When a specific item has been selected, this page will show all
    information of that item. After logging in, a user has the ability to
    select an item to update or delete its item info.'''
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('item.html', category=category, item=item)


@app.route('/catalog/items/new/', methods=['GET','POST'])
def newItem():
    '''After logging in, this page gives the user the ability to add an item
    with item info.'''
    if request.method == 'POST':
        newObj = Item(name = request.form['name'],
                category_id = request.form['category'],
                description = request.form['description'])
        session.add(newObj)
        # TODO: Flash message
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        categories = session.query(Category).all()
        return render_template('item_new.html', categories=categories)


@app.route('/catalog/<item_id>/edit/')
def editItem(item_id):
    '''After logging in, this page gives the user the ability to update the item info.'''
    categories = session.query(Category).all()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('item_edit.html', categories=categories, item=item)


@app.route('/catalog/<int:item_id>/delete/')
def deleteItem(item_id):
    '''After logging in, this page gives the user the ability to delete the
    item info.'''
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('item_delete.html', item=item)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
