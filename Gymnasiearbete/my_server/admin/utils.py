from my_server.databasehandler import create_connection
from flask import redirect, url_for, flash, abort, session
from my_server.databasehandler import create_connection
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

#utför en sql request och hämtar samtliga resultat, inte skyddad från sql-injektioner!!! ska inte användas av användare
# sql == sql query
def sql_request(sql):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return result

# utför en sql request och hämtar samtliga resultat, skyddad från sql-injektioner, kan använads av användare
# sql == sql query
# data = data som ska sökas efter (prepared statment)
def sql_request_prepared(sql,data):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql,data)
    conn.commit()
    result = cur.fetchall()
    conn.close()
    return result

# utför en sql request som skapar en till användare i tabellen users
# user = användaren som ska skapas
def insert_user(user):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name,username,email,password,admin) VALUES (?,?,?,?,?)',user)
    conn.commit()
    conn.close()
