from flask import redirect, url_for, session, request, Blueprint
from flask import render_template as rt
from my_server.shop.utils import sql_request, sql_request_prepared
from my_server.models import Category, Product, Picture
import json

shop = Blueprint('shop',__name__)


@shop.route('/categories')
@shop.route('/categories/')
@shop.route('/categories/<id>')
def categories(id = 0):
    #main_category = 0 -> huvudkategorier
    #sql_request_prepared('SELECT name, main_category FROM categories WHERE main_category = ?',(id,))
    return rt('categories.html', categories=Category.query.filter_by(id=id).first())

@shop.route('/products')
@shop.route('/products/')
@shop.route('/products/<category>')
def products(category=0):
    if 'search_data' in session:
        data = session['search_data']
        session.pop('search_data')
        return rt('products.html',products=data)
    elif category == 0:
        #sql_request('SELECT * FROM products')
        products = Product.query.all()
        print(products)
        return rt('products.html',products=products)
    #sql_request_prepared('SELECT * FROM products WHERE category = ?',(category,))
    print(Product.query.filter_by(category=category).all())
    return rt('products.html',products=Product.query.filter_by(category=category).all())

@shop.route('/product/<id>')
def product(id = 0):
    #product = sql_request_prepared('SELECT * FROM products WHERE id = ?',(id,))
    #pictures = sql_request_prepared('SELECT filepath FROM pictures WHERE product_id = ?',(id,))
    return rt('product.html',product=Product.query.filter_by(id=id).first(),pictures=Picture.query.filter_by(product_id=id).all())

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
        products = Product.query.filter(Product.name.like('%'+search+'%')).all()
        categories = Category.query.filter(Category.name.like('%'+search+'%')).all()
        #TODO: HUR!!!!!!!!!!!!!!!!
        print(json.dumps((products, categories)))
        return json.dumps((products, categories))
    else:
        session['search_data']=Product.query.filter(Product.name.like('%'+search+'%')).all()
        return redirect(url_for('shop.products'))