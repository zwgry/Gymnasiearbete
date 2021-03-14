from flask import Blueprint
from flask import render_template as rt
from my_server.models import Category
from my_server.errors.utils import is_logged_in, get_current_user

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(401)
def handle_401(err):
    return rt('errors/401.html',categories = Category.query.filter(Category.name!='Main').all(), logged_id=is_logged_in(), user=get_current_user()), 401

@errors.app_errorhandler(404)
def handle_404(err):
    return rt('errors/404.html',categories = Category.query.filter(Category.name!='Main').all(), logged_id=is_logged_in(), user=get_current_user()), 404

@errors.app_errorhandler(405)
def handle_405(err):
    return rt('errors/405.html',categories = Category.query.filter(Category.name!='Main').all(), logged_id=is_logged_in(), user=get_current_user()), 405


@errors.app_errorhandler(500)
def handle_500(err):
    return rt('errors/500.html',categories = Category.query.filter(Category.name!='Main').all(), logged_id=is_logged_in(), user=get_current_user()), 500