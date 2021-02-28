from flask import redirect, url_for, session, flash
from functools import wraps
from my_server import mail
from flask_mail import Message

def send_email(user):
    token = user.get_verification_token()
    msg = Message('Verifikationsmail',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''För att bekräfta din mail klicka på länken nedan:
{url_for('users.confirm_token', token=token, _external=True)}'''
    mail.send(msg)

# kollar om användaren är inloggad
def login_required(f):
    @wraps(f)
    def wraped(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            flash('Du måste vara inloggad för att kunna göra detta!', 'warning')
            return redirect(url_for('users.login'))
    return wraped

# kollar om användaren är utloggad
def no_login(f):
    @wraps(f)
    def wraped(*args, **kwargs):
        if 'logged_in' not in session:
            return f(*args,**kwargs)
        else:
            flash('Du kan inte vara inloggad för att kunna göra detta!', 'warning')
            return redirect(url_for('main.start'))
    return wraped

