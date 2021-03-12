from flask import session

def is_logged_in():
    if 'logged_in' in session:
        return True
    return False