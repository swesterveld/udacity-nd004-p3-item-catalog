from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = """M}XUZoTl+U3]j`Gk&d5ysi5)}GTIDA?9"""

@app.route('/')
def showCatalog():
    return "This page will show all current catagories along with the latest added items."

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
