from flask import redirect, url_for, session, request, Blueprint
from flask import render_template as rt
from my_server.shop.utils import sql_request, sql_request_prepared, sql_to_list
from my_server.models import Category, Product, Picture
import json

shop = Blueprint('shop',__name__)


@shop.route('/categories')
@shop.route('/categories/')
@shop.route('/categories/<id>')
def categories(id = 1):
    return rt('categories.html', categories=Category.query.filter_by(id=id).all())

@shop.route('/products')
@shop.route('/products/')
@shop.route('/products/<category>')
def products(category=0):
    if 'search_data' in session:
        data = session['search_data']
        session.pop('search_data')
        return rt('products.html',products=data)
    elif category == 0:
        products = Product.query.all()
        print(products)
        return rt('products.html',products=products)
    return rt('products.html',products=Product.query.filter_by(category=category).all())

@shop.route('/product/<id>')
def product(id = 0):
    return rt('product.html',product=Product.query.filter_by(id=id).first(),pictures=Picture.query.filter_by(product_id=id).all())

#inmatning till sökfunktionen är en string -> produkten / kategorins namn
#TODO: skriv klart get funktionen så att den oxå kan skicka data från sökning
@shop.route('/search_products_categories', methods = ['POST','GET'])
@shop.route('/search_products_categories/<search>')
def search(search = ''):
    #borde fungera
    if request.method == 'POST':
        search = request.form['parameter']
        if search == '': 
            return json.dumps('empty')
        products = Product.query.filter(Product.name.like('%'+search+'%')).all()
        categories = Category.query.filter(Category.name.like('%'+search+'%')).all()
        return json.dumps((sql_to_list(products),sql_to_list(categories)))
    else:
        session['search_data']=Product.query.filter(Product.name.like('%'+search+'%')).all()
        return redirect(url_for('shop.products'))

@shop.route('/sort', methods = ['POST'])
def sort_search(category=0,order=''):
    search = request.form['serach']
    if search != '':
        if order == 'ASC':
            products = Product.query.filter(Product.category.like(category)).order_by(Product.price.asc()).all()
            return json.dumps(sql_to_list(products))
        elif order == 'DESC':
            products = Product.query.filter(Product.category.like(category)).order_by(Product.price.dsc()).all()
            return json.dumps(sql_to_list(products))
    return json.dumps('Fel vid sortering, kontrollera inmatning')