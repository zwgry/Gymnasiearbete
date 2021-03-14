from flask import Blueprint
from flask import render_template as rt

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def handle_404(err):
    return rt('errors/404.html'), 404

@errors.app_errorhandler(500)
def handle_500(err):
    return rt('errors/500.html'), 500