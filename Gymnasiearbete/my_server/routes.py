from my_server import app
from flask import render_template as rt
from flask import request, redirect, url_for,flash, abort, session
from my_server.databasehandler import create_connection
import bcrypt
import json

#db_test.db ligger i gitignore !!!!!!
#TODO: innan inlämning gör en 'riktig' databas med lite bättre struktur och namn

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

@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/start')
def start():
    return rt('index.html')


@app.route('/categories')
@app.route('/categories/')
@app.route('/categories/<id>')
def categories(id = 0):
    #main_category = 0 -> huvudkategorier
    return rt('categories.html', categories=sql_request_prepared('SELECT name, main_category FROM categories WHERE main_category = ?',(id,)))

@app.route('/products')
@app.route('/products/')
@app.route('/products/<category>')
def products(category=0):
    if 'search_data' in session:
        data = session['search_data']
        session.pop('search_data')
        return rt('products.html',products=data)
    elif category == 0:
        return rt('products.html',products=sql_request('SELECT * FROM products'))
    return rt('products.html',products=sql_request_prepared('SELECT * FROM products WHERE category = ?',(category,)))

@app.route('/product/<id>')
def product(id = 0):
    product = sql_request_prepared('SELECT * FROM products WHERE id = ?',(id,))
    pictures = sql_request_prepared('SELECT filepath FROM pictures WHERE product_id = ?',(id,))
    return rt('product.html',product=product,pictures=pictures)

#inmatning till sökfunktionen är en string -> produkten / kategorins namn
#TODO: skriv klart get funktionen så att den oxå kan skicka data från sökning
@app.route('/search_products_categories', methods = ['POST','GET'])
@app.route('/search_products_categories/<search>')
def search(search = ''):
    #borde fungera
    if request.method == 'POST':
        search = request.form['parameter']
        if search == "": 
            return json.dumps("empty")
        products = sql_request_prepared('SELECT * FROM products WHERE name LIKE ?',('%'+search+'%',))
        categories = sql_request_prepared('SELECT * FROM categories WHERE name LIKE ?',('%'+search+'%',))
        print(json.dumps((products, categories)))
        return json.dumps((products, categories))
    else:
        session['search_data']=sql_request_prepared('SELECT * FROM products WHERE name LIKE ?',('%'+search+'%',))
        return redirect(url_for('products'))
        #return rt('products.html',product=sql_request_prepared('SELECT * FROM products WHERE name LIKE ?',('%'+search+'%',)))

#Klar??
@app.route('/login', methods=['GET','POST'])
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
                    return redirect(url_for('start'))
        flash('användarnamnet eller lösenordet är felaktigt','warning')
    return rt('login.html')

#Klar?
@app.route('/logout')
def logout():
    session.pop('username',None)
    session['logged_in'] = False
    flash('Du har loggats ut','info')
    return redirect(url_for('start'))

#TODO: klart denna funktion
#Klar??
@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
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
            return redirect(url_for('login'))
    else:
        return rt('sign_up.html')

@app.route('/admin')
def admin():
    if session['logged_in'] == False:
        print(session['logged_in'])
        return redirect(url_for('login'))
    admin = sql_request_prepared('SELECT admin FROM users WHERE username like ?',(session['username'],)) 
    if admin[0][0] != 1:
        abort(401)
    return rt('admin.html')
