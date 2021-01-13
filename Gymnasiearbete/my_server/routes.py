from my_server import app
from flask import render_template as rt
from flask import request, redirect, url_for,flash, abort, session
from my_server.databeasehandler import create_connection

@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/start')
def start():
    return rt('index.html')


@app.route('/categories')
def categories():
    pass

@app.route('/category/<id>')
def category(id=None):
    if  id==None:
        return redirect(url_for('categories'))
    #TODO: skapa resten av denna route så att rätt kategori renderas
    pass

@app.route('/products')
def products():
    pass

@app.route('/product/<id>')
def product(id=None):
    if id==None:
        return redirect(url_for('products'))
    #TODO: skapa resten av denna route så att rätt produkt renderas
    pass


