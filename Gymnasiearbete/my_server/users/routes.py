from flask import redirect, url_for, request, flash, session, Blueprint
from flask import render_template as rt
from my_server.users.utils import no_login, login_required, sql_request, insert_user
from my_server import db
from my_server.models import User
import bcrypt

users = Blueprint('users',__name__)

@users.route('/login', methods=['GET','POST'])
@no_login
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = User.query.all()
        for user in users:
            if user.username == username:
                if bcrypt.checkpw(password.encode('utf-8'),user.password):
                    flash('inloggad','success')
                    session['username'] = username
                    session['logged_in'] = True
                    return redirect(url_for('main.start'))
        flash('användarnamnet eller lösenordet är felaktigt','warning')
    return rt('login.html')

#Klar?
@users.route('/logout')
@login_required
def logout():
    session.clear()
    flash('Du har loggats ut','info')
    return redirect(url_for('main.start'))

@users.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        f_name = request.form['fname']
        l_name = request.form['lname']
        username = request.form['uname']
        email = request.form['email']
        password = request.form['password1']
        password2 = request.form['password2']
        current_users = User.query.all()
        for user in current_users:
            if user.username == username:
                flash('användarnamnet används redan','warning')
                return rt('sign_up.html')
            elif user.email == email:
                flash('mailen används redan','warning')
                return rt('sign_up.html')
        if password == password2:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
            new_user = User(username=username,name=f_name+' '+l_name,email=email,password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('användare skapad','success')
            return redirect(url_for('users.login'))
    else:
        return rt('sign_up.html')

