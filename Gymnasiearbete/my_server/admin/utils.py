from flask import redirect, url_for, flash, abort, session
from my_server.models import User
from functools import wraps
from my_server import mail
from flask_mail import Message

def send_newsletter(subject,content,recipients):
    msg = Message(subject,
                  sender='noreply@demo.com',
                  recipients=recipients)
    msg.body = content
    mail.send(msg)

def is_logged_in():
    if 'logged_in' in session:
        return True
    return False

# kollar om användaren är en admin
def admin_required(f):
    @wraps(f)
    def wraped(*args, **kwargs):
        if 'logged_in' in session:
            if session['logged_in'] == False:
                print(session['logged_in'])
                return redirect(url_for('users.login'))
            admin = User.query.filter_by(username=session['username']).first()
            if admin.admin == False:
                return abort(401)
            else:
                return f(*args,**kwargs)
        else:
            return abort(401)
    
    return wraped