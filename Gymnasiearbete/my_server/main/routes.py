from flask import Blueprint
from flask import render_template as rt 
from my_server.models import Category, Product, Picture
from my_server.main.utils import is_logged_in, get_current_user
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
    iterations = 10
    i = 0
    while i < iterations:
        id = randint(1,Product.query.count())
        if id not in products_id:
            product = Product.query.filter_by(id=id).first()
            if product is not None:
                products_id.append(id)
                products.append(product)
                i += 1
    for id in products_id:
        pictures.append(Picture.query.filter_by(product_id=id).first())
    return rt('index.html',products=products,pictures=pictures,logged_id=is_logged_in(), user=get_current_user(), categories = Category.query.all())