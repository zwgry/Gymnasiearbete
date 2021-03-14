from flask import session
from my_server.models import User

def is_logged_in():
    if 'logged_in' in session:
        return True
    return False

def get_current_user():
    if is_logged_in():
        username = session['username']
        user = User.query.filter_by(username=username).first()
        return user
    return None