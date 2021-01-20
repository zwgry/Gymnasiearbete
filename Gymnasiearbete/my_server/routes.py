from my_server import app
from flask import render_template as rt
from flask import request, redirect, url_for,flash, abort, session
from my_server.databasehandler import create_connection
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
        search = request.form['search']
        products = sql_request_prepared('SELECT * FROM products WHERE name LIKE ?',('%'+search+'%',))
        categories = sql_request_prepared('SELECT * FROM categories WHERE name LIKE ?',('%'+search+'%',))
        return json.dumps({'products':products,'categories':categories})
    else:
        session['search_data']=sql_request_prepared('SELECT * FROM products WHERE name LIKE ?',('%'+search+'%',))
        return redirect(url_for('products'))
        #return rt('products.html',product=sql_request_prepared('SELECT * FROM products WHERE name LIKE ?',('%'+search+'%',)))

#TODO: klart denna funktion
#ska kolla om användaren finns först
#sen skapa användaren (med hashat lösenord)
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
                flash('NAMMMMMMMMMMMMMMN','warning')
                return rt('sign_up.html')
            elif user[1] == email:
                flash('mAILLLLLLLLLLLLLLLLLL','warning')
                return rt('sign_up.html')
        #MÅSTE HASHAS
        if password == password2:
            new_user=(f_name+' ' +l_name,username,email,password)
            #conn = create_connection()
            #cur = conn.cursor()
            #cur.execute('INSERT INTO users (name,username,email,password) VALUES (?,?,?,?)', new_user)
            #conn.commit()
            #conn.close()
            #skriv klart
            return f'{new_user}'
    else:
        return rt('sign_up.html')
