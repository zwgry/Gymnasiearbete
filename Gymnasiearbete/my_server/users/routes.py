from flask import redirect, url_for, request, flash, session, Blueprint
from flask import render_template as rt
from my_server.users.utils import no_login, login_required, sql_request, insert_user
import bcrypt

users = Blueprint('users',__name__)

#Klar??
@users.route('/login', methods=['GET','POST'])
@no_login
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = sql_request('SELECT username,password FROM users')
        for user in users:
            if user[0] == username:
                if bcrypt.checkpw(password.encode('utf-8'),user[1]): #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
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
    #gc.collect()
    flash('Du har loggats ut','info')
    return redirect(url_for('main.start'))

#TODO: klart denna funktion
#Klar??
@users.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        f_name = request.form['fname']
        l_name = request.form['lname']
        username = request.form['uname']
        email = request.form['email']
        password = request.form['password1']
        password2 = request.form['password2']
        current_users = sql_request('SELECT username,email FROM users')
        for user in current_users:
            if user[0] == username:
                flash('användarnamnet används redan','warning')
                return rt('sign_up.html')
            elif user[1] == email:
                flash('mailen används redan','warning')
                return rt('sign_up.html')
        if password == password2:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
            new_user=(f_name+' ' +l_name,username,email,hashed_password,0)
            insert_user(new_user)
            flash('användare skapad','success')
            return redirect(url_for('users.login'))
    else:
        return rt('sign_up.html')

