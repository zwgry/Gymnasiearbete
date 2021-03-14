from flask import redirect, url_for, session, request, Blueprint, make_response
from flask import render_template as rt
from my_server.shop.utils import is_logged_in, sql_to_list, get_current_user
from my_server.models import Category, Product, Picture
from my_server import db
import json

shop = Blueprint('shop',__name__)

@shop.route('/products')
@shop.route('/products/<category>')
def products(category=0):
    if 'search_data' in session:
        data = session['search_data']
        session.pop('search_data')
        return rt('products.html',products=data)
    elif category == 0:
        products = Product.query.all()
        return rt('products.html',products=products)
    return rt('products.html',products=Product.query.filter_by(category=category).all(),logged_id=is_logged_in(),category=Category.query.filter_by(id=category).first(),user=get_current_user(), categories = Category.query.all())

@shop.route('/product/<id>')
def product(id = 0):
    return rt('product.html',product=Product.query.filter_by(id=id).first(),pictures=Picture.query.filter_by(product_id=id).all(),logged_id=is_logged_in(),user=get_current_user(), categories = Category.query.all())

#inmatning till sökfunktionen är en string -> produkten / kategorins namn
@shop.route('/search_products_categories', methods = ['POST','GET'])
@shop.route('/search_products_categories/<search>')
def search(search = ''):
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

@shop.route('/checkout')
def checkout():
    return rt('checkout.html', logged_id=is_logged_in(),user=get_current_user())

@shop.route('/sort', methods = ['POST'])
def sort_search(category=0,order=''):
    category = request.form['category']
    order = request.form['order']
    if search != '':
        if order == 'ASC':
            products = Product.query.filter(Product.category.like(category)).order_by(Product.price.asc()).all()
            pictures = Picture.query.group_by(Picture.product_id).all()
            return json.dumps((sql_to_list(products),sql_to_list(pictures)))
        elif order == 'DSC':
            products = Product.query.filter(Product.category.like(category)).order_by(Product.price.desc()).all()
            pictures = Picture.query.group_by(Picture.product_id).all()
            return json.dumps((sql_to_list(products),sql_to_list(pictures)))
    return json.dumps('Fel vid sortering, kontrollera inmatning')

@shop.route('/cookie_products')
def cookie_ajax():
    cookie = json.loads(request.args['data'])
    if cookie == '':
        return json.dumps("error")
    ids = []
    amounts = []
    for product in cookie:
        if product[0] in ids:
            position = ids.index(product[0])
            amounts[position] += product[1]
        else:
            ids.append(product[0])
            amounts.append(product[1])
    products = Product.query.all()
    products_requested = []
    for product in products:
        if product.id in ids:
            product_dict = product.as_dict()
            product_dict['stock']=amounts[ids.index(product.id)]
            products_requested.append(product_dict)
    return json.dumps(products_requested)
