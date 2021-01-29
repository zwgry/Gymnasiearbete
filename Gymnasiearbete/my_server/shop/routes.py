from flask import redirect, url_for, session, request, Blueprint
from flask import render_template as rt
from my_server.shop.utils import sql_request, sql_request_prepared
import json

shop = Blueprint('shop',__name__)


@shop.route('/categories')
@shop.route('/categories/')
@shop.route('/categories/<id>')
def categories(id = 0):
    #main_category = 0 -> huvudkategorier
    return rt('categories.html', categories=sql_request_prepared('SELECT name, main_category FROM categories WHERE main_category = ?',(id,)))

@shop.route('/products')
@shop.route('/products/')
@shop.route('/products/<category>')
def products(category=0):
    if 'search_data' in session:
        data = session['search_data']
        session.pop('search_data')
        return rt('products.html',products=data)
    elif category == 0:
        return rt('products.html',products=sql_request('SELECT * FROM products'))
    return rt('products.html',products=sql_request_prepared('SELECT * FROM products WHERE category = ?',(category,)))

@shop.route('/product/<id>')
def product(id = 0):
    product = sql_request_prepared('SELECT * FROM products WHERE id = ?',(id,))
    pictures = sql_request_prepared('SELECT filepath FROM pictures WHERE product_id = ?',(id,))
    return rt('product.html',product=product,pictures=pictures)

#inmatning till sökfunktionen är en string -> produkten / kategorins namn
#TODO: skriv klart get funktionen så att den oxå kan skicka data från sökning
@shop.route('/search_products_categories', methods = ['POST','GET'])
@shop.route('/search_products_categories/<search>')
def search(search = ''):
    #borde fungera
    if request.method == 'POST':
        search = request.form['parameter']
        if search == "": 
            return json.dumps("empty")
        products = sql_request_prepared('SELECT * FROM products WHERE name LIKE ?',('%'+search+'%',))
        categories = sql_request_prepared('SELECT * FROM categories WHERE name LIKE ?',('%'+search+'%',))
        print(json.dumps((products, categories)))
        return json.dumps((products, categories))
    else:
        session['search_data']=sql_request_prepared('SELECT * FROM products WHERE name LIKE ?',('%'+search+'%',))
        return redirect(url_for('shop.products'))