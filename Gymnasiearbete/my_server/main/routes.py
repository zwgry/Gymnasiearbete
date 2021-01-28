from flask import Blueprint
from flask import render_template as rt 

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
@main.route('/home')
@main.route('/start')
def start():
    return rt('index.html')