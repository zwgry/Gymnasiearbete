from my_server import app
from flask import render_template as rt
from flask import request, redirect, url_for,flash, abort, session
from my_server.databasehandler import create_connection

#db_test.db ligger i gitignore !!!!!!

@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/start')
def start():
    return rt('index.html')


@app.route('/categories')
def categories():
    sql = 'SELECT name, main_category FROM categories WHERE main_category = 1'
    con = create_connection()
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchall()

    return f'<h1>{result}</h1>'

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


