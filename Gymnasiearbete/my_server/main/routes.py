from flask import Blueprint
from flask import render_template as rt 
from my_server.models import Category, Product, Picture
from my_server.main.utils import is_logged_in
from random import randint

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
@main.route('/home')
@main.route('/start')
def start():
    products_id = []
    products = []
    pictures = []
    for i in range(6):
        products_id.append(randint(1,Product.query.count()))
    for id in products_id:
        products.append(Product.query.filter_by(id=id).first())
        pictures.append(Picture.query.filter_by(product_id=id).first())
    return rt('index.html',products=products,pictures=pictures,logged_id=is_logged_in())