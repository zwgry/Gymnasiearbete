from my_server import app
from flask import render_template as rt
from flask import request, redirect, url_for,flash, abort, session
from my_server.databasehandler import create_connection

#db_test.db ligger i gitignore !!!!!!
def sql_request(sql):
    con = create_connection()
    cur = con.cursor()
    cur.execute(sql)
    return cur.fetchall()

def sql_request_prepared(sql,data):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql,data)
    conn.commit()
    return cur.fetchall()

@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/start')
def start():
    return rt('index.html')


@app.route('/categories')
@app.route('/categories/')
@app.route('/categories/<id>')
def categories(id = 0):
    if request.method == 'POST':
        #sök efter kategorier
        pass
    else:
        #main_category = 0 -> huvudkategorier
        return rt('categories.html', categories=sql_request_prepared('SELECT name, main_category FROM categories WHERE main_category = ?',(id,)))

@app.route('/get_categories_post', methods = ['GET,POST'])
def categories_post():
    if request.method == 'POST':
            #sök efter produkter
            return '<h1>aaaaaaaaaaaaaaa</h1>'


@app.route('/products')
@app.route('/products/')
@app.route('/products/<id>')
def products(id=0):
    if id == 0:
        return rt('products.html',products=sql_request('SELECT name FROM products'))
    return rt('products.html',products=sql_request_prepared('SELECT name, category FROM products WHERE category = ?',(id,)))

@app.route('/get_products_post', methods = ['GET,POST'])
def products_post():
    #gör om
    if request.method == 'POST':
        action = request.form['action']
        if action == 'search':
            search = request.form['input']
            response = sql_request_prepared('SELECT * FROM products WHERE name = ?',(search,))
            return rt('products.html',products=response)
        elif action == 'sort':
            type = request.form['type']
            if type == 'cheapest':
                pass
            else:
                pass
        return '<h1>aaaaaaaaaaaaaaa</h1>'

@app.route('/search_products_categories', methods = ['GET,POST'])
@app.route('/search_products_categories/<search>', methods = ['GET'])
def search(search = ''):
    if request.method == 'POST':
        pass
    else:
        pass
