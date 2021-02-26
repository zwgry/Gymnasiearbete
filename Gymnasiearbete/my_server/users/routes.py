from flask import redirect, url_for, request, flash, session, Blueprint
from flask import render_template as rt
from my_server.users.utils import no_login, login_required, sql_request, insert_user
from my_server import db
from my_server.models import User
from my_server.token import generate_confirmation_token, confirm_token
import datetime
from my_server.email import send_email
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


            token = generate_confirmation_token(new_user.email)
            confirm_url = url_for('users.confirm_email', token=token, _external=True)
            html = rt('email/confirm.html', confirm_url=confirm_url)
            subject = "Please confirm your email"
            send_email(new_user.email, subject, html)
            flash('användare skapad, vi har skickat ett bekräftelsemail till din mailadress','success')
            return redirect(url_for('users.login'))
    else:
        return rt('sign_up.html')


@users.route('/confirm/<token>')
@login_required
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        users.confirmed = True
        users.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('Din main är nu verifierad! Tack!', 'success')
    return redirect(url_for('main.start'))


