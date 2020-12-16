#TODO: gör färdigt databasen och lägg till några fler testkategorier
from my_server.databasehandler import create_connection

conn = create_connection()
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL    
)''')

new_products = [
    ('Tangentbord','Ett tangentbord som har flera olika fina knappar. Det finns i flera olika färger'),
    ('Mus','En mus, som har två knappar')
    ]

cur.executemany('INSERT INTO products (name,description) VALUES (?,?)',new_products)

cur.execute('''CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    main_category INTEGER REFERENCES categories(id)
)''')

new_categories = [
    ('Datortillbehör','Här finns alla datortilbehör','NULL'),
    ('Tangentbord','Här visas alla olika tangetbord som finns',1)
    ]

cur.executemany('INSERT INTO categories (name,description,main_category) VALUES (?,?,?)', new_categories)

cur.execute('''CREATE TABLE IF NOT EXISTS produts_categories (
    id INTEGER PRIMARY KEY,
    product_id INTEGER REFERENCES product(id),
    category_id INTEGER REFERENCES category(id)
)''')

new_products_categories = [(1,1),(1,2)]

cur.executemany('INSERT INTO produts_categories (')


cur.execute('''CREATE TABLE IF NOT EXISTS pictures (
    id INTEGER PRIMARY KEY,
    filepath TEXT NOT NULL
)''')

new_pictures = [
    ('apa.png',),
    ('apa2.png',),
    ('apa3.png',)
    ]

cur.executemany('INSERT INTO pictures (filepath) VALUES (?)', new_pictures)

cur.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)''')

new_users = [('admin','admin','admin','admin'),('Mathias','mathias','mathias.wistrom@edu.nacka.se','lösen123'),('Lukas','lukas','lukas.strand@edu.nacka.se','lösen123')]

cur.executemany('INSERT INTO users (name,username,email,password) VALUES (?,?,?,?)', new_users)

cur.execute('''CREATE TABLE IF NOT EXISTS lists (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    name TEXT NOT NULL
)''')

new_lists = [(2,'test'),(2,'test'),(3,'test')]

cur.executemany('INSERT INTO lists (user_id,name) VALUES (?,?)', new_lists)

cur.execute('''CREATE TABLE IF NOT EXISTS items_lists (
    id INTEGER PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    list_id INTEGER REFERENCES list(id)
)''')

new_items_lists = [(1,1),(1,2),(2,1)]

cur.executemany('INSERT INTO items_lists (product_id,list_id) VALUES (?,?)', new_items_lists)

conn.commit()
conn.close()
