from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = """M}XUZoTl+U3]j`Gk&d5ysi5)}GTIDA?9"""

@app.route('/')
@app.route('/catalog/')
def showCatalog():
    return "This is the homepage which will show all current categories along with the latest added items. After logging in, a user has the ability to add, update or delete item info."


@app.route('/catalog.json')
def showCatalogJSON():
    return "This is the JSON endpoint provided by the application."


@app.route('/catalog/<category>/')
@app.route('/catalog/<category>/items/')
def showCategory(category):
    return "When a specific category has been selected, this page will show all the items available for that category."


@app.route('/catalog/<category>/<item>/')
def showItem(category, item):
    return "When a specific item has been selected, this page will show all information of that item. After logging in, a user has the ability to select an item to update or delete its item info."


@app.route('/catalog/items/new/')
def newItem():
    return "After logging in, this page gives the user the ability to add an item with item info."


@app.route('/catalog/<item>/edit/')
def editItem(item):
    return "After logging in, this page gives the user the ability to update the item info."


@app.route('/catalog/<item>/delete/')
def deleteItem(item):
    return "After logging in, this page gives the user the ability to delete the item info."


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
