from flask import redirect, url_for, request, flash, session, Blueprint
from flask import render_template as rt
from my_server.users.utils import no_login, login_required,send_email, is_logged_in, get_current_user
from my_server import db
from my_server.models import User, Category, Newsletter_Recipients
import datetime
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
                    flash('Inloggad','success')
                    session['username'] = username
                    session['logged_in'] = True
                    return redirect(url_for('main.start'))
        flash('Användarnamnet och/eller lösenordet är felaktigt!','warning')
    return rt('login.html',logged_id=is_logged_in(),user=get_current_user(),categories = Category.query.all())

@users.route('/edit_profile', methods=['GET','POST'])
@login_required
def edit_user():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        id = request.form['id']
        user = User.query.filter_by(id=id).first()
        user.username = username
        user.name = name
        user.email = email
        db.session.commit()
        return rt('edit_user.html', user = user,logged_id=is_logged_in(),categories = Category.query.all())
    user_id = request.args['id']
    user = User.query.filter_by(id=user_id).first()
    return rt('edit_user.html', user = user,logged_id=is_logged_in(),categories = Category.query.all())

@users.route('/logout')
@login_required
def logout():
    session.clear()
    flash('Du har loggats ut','info')
    return redirect(url_for('main.start'))

@users.route('/register', methods=['GET','POST'])
@no_login
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
                flash('Användarnamnet används redan','warning')
                return rt('sign_up.html',categories = Category.query.all())
            elif user.email == email:
                flash('Mailen används redan','warning')
                return rt('sign_up.html',categories = Category.query.all())
        if password == password2:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
            new_user = User(username=username,name=f_name+' '+l_name,email=email,password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            send_email(new_user)
            flash('Användare skapad, vi har skickat ett bekräftelsemail till din mailadress','success')
            return redirect(url_for('users.login'))
    else:
        return rt('sign_up.html',logged_id=is_logged_in(),user=get_current_user(),categories = Category.query.all())

@users.route('/newsletter/register', methods = ['POST','GET'])
def newsletter_registration():
    if request.method == 'POST':
        email = request.form['email']
        if email == '':
            flash('Du måste skriva in din mail','warning')
            return rt('newsletter_registration.html',logged_id=is_logged_in(),user=get_current_user(),categories = Category.query.all())
        for recipient in Newsletter_Recipients.query.all():
            if recipient.email == email:
                flash('Mailen är redan registrerad','warning')
                return rt('newsletter_registration.html',logged_id=is_logged_in(),user=get_current_user(),categories = Category.query.all())
        nlr = Newsletter_Recipients(email=email)
        db.session.add(nlr)
        db.session.commit()
        flash('Mail är nu registrerad','success')
    return rt('newsletter_registration.html',logged_id=is_logged_in(),user=get_current_user(),categories = Category.query.all())

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def confirm_token(token):
    if not session.get('username') is None:
        current_user = User.query.filter_by(username=session['username']).first()
        if current_user.confirmed:
            flash('Du är redan verifierad','info')
            return redirect(url_for('main.start'))
    user = User.verify_verification_token(token)
    if user is None:
        flash('Felaktig eller gammal länk, försök igen', 'warning')
        return redirect(url_for('main.start'))
    else:
        user.confirmed = True
        db.session.commit()
    flash('Du är nu verifierad!','success')
    return redirect(url_for('main.start'))


