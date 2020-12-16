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
    ('SteelSeries Apex Pro','Spela mer exakt, snabbt och säkert med världens första mekaniska tangentbord med OmniPoint mekaniska brytare. Varje enskild tangent kan tweakas för att möta önskad aktivering, från världens snabbaste fjäderlätta tryckningar till de hårda och djupa. Tangentbordet är även utrustat med en Smart Oled-Display, en integrerad kommandocentral för att justera inställningar, få info direkt från ditt spel, musik eller Discord så att du skall slippa avbryta ditt spel.'),
    ('Ducky One 2 Mini','Ducky One 2 Mini blev precis lite bättre. 2020 års modell har ett förbättrat kretskort och extra belysning under mellanslagstangenten. Dessutom har firmware skrivits om för en mer stabil skrivupplevelse."\n"Ducky One 2 Mini är utrustat med MX Cherry brytare och högkvalitativa tangenter i PBT-plast vilket tar kvalitén till en ny nivå. De 5 robusta gummidynorna och 2 gummifötterna ser till att tangentbordet stannar på plats under dina spelsessioner.'),
    ('Logitech G Pro Gaming Keyboard','Detta tangentbord är designat efter de exakta specifikationerna som efterfrågas av världens bästa e-sportare. Det är utrustat med brytarna GX-Blue som erbjuder en klickig upplevelse vilket är efterfrågat av många e-sportsproffs. Utöver formatet i TKL erbjuder även detta tangentbord Logitechs anpassningsbara LIGHTSYNC och en avtagbar mikro-USB-kabel.')
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

cur.executemany('INSERT INTO produts_categories (product_id,category_id) VALUES (?,?)', new_products_categories)

cur.execute('''CREATE TABLE IF NOT EXISTS pictures (
    id INTEGER PRIMARY KEY,
    filepath TEXT NOT NULL
)''')

pictures_location = 'Gymnasiearbete\my_server\static\images'

new_pictures = [
    ('my_server\static\imagesp1i1.jpg',),
    ('my_server\static\imagesp1i2.jpg',),
    ('my_server\static\imagesp1i3.jpg',),
    ('my_server\static\imagesp2i1.jpg',),
    ('my_server\static\imagesp2i2.jpg',),
    ('my_server\static\imagesp2i3.jpg',),
    ('my_server\static\imagesp3i1.jpg',),
    ('my_server\static\imagesp3i2.jpg',),
    ('my_server\static\imagesp3i3.jpg',)
    ]

cur.executemany('INSERT INTO pictures (filepath) VALUES (?)', new_pictures)

cur.execute('''CREATE TABLE IF NOT EXISTS products_pictures (
    id INTEGER PRIMARY KEY,
    product_id INTEGER REFERENCES product(id),
    picture_id INTEGER REFERENCES picture(id)
)''')

new_products_pictures = [(1,1),(1,2),(1,3),(2,4),(2,5),(2,6),(3,7),(3,8),(3,9)]

cur.executemany('INSERT INTO products_pictures (product_id,picture_id) VALUES (?,?)', new_products_pictures)

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
