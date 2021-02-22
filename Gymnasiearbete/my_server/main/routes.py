from flask import Blueprint
from flask import render_template as rt 
from my_server.models import Category, Product, Picture

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
@main.route('/home')
@main.route('/start')
def start():
    #Skicka bilder till index
    return rt('index.html')