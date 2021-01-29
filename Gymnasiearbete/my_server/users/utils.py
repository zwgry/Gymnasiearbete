from my_server.databasehandler import create_connection
from flask import redirect, url_for, session, flash
from functools import wraps

#utför en sql request och hämtar samtliga resultat, inte skyddad från sql-injektioner!!! ska inte användas av användare
# sql == sql query
def sql_request(sql):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql)
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

