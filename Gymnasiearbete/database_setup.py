#TODO: gör färdigt databasen och lägg till några fler testkategorier
from my_server.databasehandler import create_connection

conn = create_connection()
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL    
)''')

new_products = [
    ('Tangentbord','Ett tangentbord som har flera olika fina knappar. Det finns i flera olika färger'),
    ('Mus','En mus, som har två knappar')
    ]

cur.executemany('INSERT INTO product (name,description) VALUES (?,?)',new_products)

cur.execute('''CREATE TABLE IF NOT EXISTS category (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    main_category INTEGER REFERENCES category(id)
)''')

new_categories = [
    ('Datortillbehör','Här finns alla datortilbehör','NULL'),
    ('Tangentbord','Här visas alla olika tangetbord som finns',1)]

cur.executemany('INSERT INTO category (name,description,main_category) VALUES (?,?,?)', new_categories)

cur.execute('''CREATE TABLE IF NOT EXISTS pictures (
    id INTEGER PRIMARY KEY,
    filepath TEXT NOT NULL
)''')

new_pictures = [('apa.png',),('svante.png',),('apa3.png',)]

cur.executemany('INSERT INTO pictures (filepath) VALUES (?)', new_pictures)

conn.commit()
conn.close()
