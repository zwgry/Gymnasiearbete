#TODO: gör färdigt databasen och lägg till några fler testkategorier
from my_server.databasehandler import create_connection

conn = create_connection()
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    stock INTEGER NOT NULL,
    category INTEGER REFERENCES categories(id)
)''')


new_products = [
    ('SteelSeries Apex Pro','Spela mer exakt, snabbt och säkert med världens första mekaniska tangentbord med OmniPoint mekaniska brytare. Varje enskild tangent kan tweakas för att möta önskad aktivering, från världens snabbaste fjäderlätta tryckningar till de hårda och djupa. Tangentbordet är även utrustat med en Smart Oled-Display, en integrerad kommandocentral för att justera inställningar, få info direkt från ditt spel, musik eller Discord så att du skall slippa avbryta ditt spel.',15,1),
    ('Ducky One 2 Mini','Ducky One 2 Mini blev precis lite bättre. 2020 års modell har ett förbättrat kretskort och extra belysning under mellanslagstangenten. Dessutom har firmware skrivits om för en mer stabil skrivupplevelse."\n"Ducky One 2 Mini är utrustat med MX Cherry brytare och högkvalitativa tangenter i PBT-plast vilket tar kvalitén till en ny nivå. De 5 robusta gummidynorna och 2 gummifötterna ser till att tangentbordet stannar på plats under dina spelsessioner.',2,1)
    ]

"""('Logitech G Pro Gaming Keyboard','Detta tangentbord är designat efter de exakta specifikationerna som efterfrågas av världens bästa e-sportare. Det är utrustat med brytarna GX-Blue som erbjuder en klickig upplevelse vilket är efterfrågat av många e-sportsproffs. Utöver formatet i TKL erbjuder även detta tangentbord Logitechs anpassningsbara LIGHTSYNC och en avtagbar mikro-USB-kabel.'),
    ('Apple MacBook Air (2020)','Apples tunnaste och lättaste bärbara dator får nu mer kraft än någonsin tidigare. Med Apple Silicone M1-chippet är MacBook Air omgjord från grunden. Upp till 3,5 gånger snabbare processor, upp till 5 gånger snabbare grafik­processor och med Apples mest avancerade Neural Engine för upp till 9 gånger snabbare maskin­inlärning. Den har dessutom den längsta batteritiden någonsin på upp till hela 18 timmar. Dess design är lika tunn och lätt som tidigare men är nu tystare, då den helt saknar fläktar.'),
    ('ASUS ZenBook Flip 13 UX363 PURE','Nya ZenBook Flip 13 har en helt ny design som kombinerar portabilitet med mångsidighet. Den är utrustad med en FHD NanoEdge OLED-touchskärm som är lika vacker att titta på som den har flera tekniska fördelar. ZenBook Flip 13 har en premium byggkvalitet och den är slitstark, militärklassad och byggd helt i aluminium. ZenBook Flip 13 drivs av Intels nya 11:gen Tiger Lake-processor med förbättrad grafikprestanda från IRIS XE-tekniken.'),
    ('Huawei MateBook X PRO','Huawei MateBook X PRO är nu utrustad med 10:de generationens Intel-processor. Detta är en av de mest gedigna och välbyggda laptops som finns. Den är oerhört liten och smäcker, men inger ändå en enorm kvalitetskänsla. Man känner att den är tillverkad med såväl kvalitét som med kärlek. Med en batteritid som räcker hela dagen och prestanda som tuggar i sig det mesta är detta en perfekt kompanjon att ha med sig överallt.'),
    ('Lenovo Yoga Slim 7','Lenovo Yoga Slim 7 kombinerar kraften från en AMD Ryzen 5-processor med Radeon-grafik och upp till 14 timmars batteritid. Den har en FHD-bildskärm optimerad med Dolby Vision och ljud från Dolby Atmos vilket tar underhållningen till nya höjder. Den underlättar dessutom vardagen för dig med smarta och tidsbesparande funktioner som rörelsesensorer för automatisk utloggning när du lämnar datorn, batterioptimering och en röststyrd assistent som även fungerar i viloläge.'),
    ('Huawei MateBook D','Huawei MateBook D 15" är byggd av finaste metall med mjukt rundade kanter som ger ett sofistikerat intryck. Med en vikt på endast 1,53 Kg och en tjocklek på 16,9 mm tillåter den dig att vara flexibel och passar både för nytta och nöje. Med fingeravtrycksläsaren i power-knappen både startar du och loggar in på din dator i ett enda steg. Datorn laddas dessutom via USB-C.'),
    ('Acer Aspire 5','Denna dator är perfekt för dig som vill ha en snabb vardagsdator. En Core i3-processor i kombination med 4GB internminne och 128GB SSD ger dig bra med kraft för de flesta ändamålen, och den Full HD-upplösta skärmen visar alla detaljer i såväl bilder som i filmer.'),
    ('Acer Aspire XC-895','Acer Aspire XC-895 perfekt för dig som vill ha en stationär dator som klarar dagliga uppgifter och vanliga underhållning. Den är byggd i ett slimmat chassi utrustad med 10:e generationens Core i5-processor, 8GB RAM och en SSD på 512GB.'),
    ('Taurus Gaming Elite RTX 3080 - 3700X','En riktigt kraftfull gamingdator med RTX 3080 och AMD Ryzen 7 3700X. Datorn för dig som vill spela med hög FPS i tunga spel.')"""

cur.executemany('INSERT INTO products (name,description,stock,category) VALUES (?,?,?,?)',new_products)

cur.execute('''CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    main_category INTEGER REFERENCES categories(id)
)''')

new_categories = [
    ('Datortillbehör','Här finns alla datortilbehör',0),
    ('Tangentbord','Här visas alla olika tangetbord som finns',1),
    ('Datorer','Här finns alla datorer, stationära och bärbara',0),
    ('Stationära datorer','Här finns alla sationära datorer',3),
    ('Gaming','Alla gamingdatorer',4),
    ('Standard','Alla standarddatorer',4),
    ('Bärbara datorer','Här finns alla bärbara datorer',3),
    ('10-13.9"','Bärbara datorer som är mellan 10 och 14 tum',7),
    ('14-14.9"','Bärbara datorer som är mellan 14 och 15 tum',7),
    ('15-16.9"','Bärbara datorer som är mellan 15 och 17 tum',7)
    ]

cur.executemany('INSERT INTO categories (name,description,main_category) VALUES (?,?,?)', new_categories)

#Ta bort kanske?
cur.execute('''CREATE TABLE IF NOT EXISTS produts_categories (
    id INTEGER PRIMARY KEY,
    product_id INTEGER REFERENCES product(id),
    category_id INTEGER REFERENCES category(id)
)''')

new_products_categories = [(1,2),(2,2),(2,3),(4,8),(5,8),(6,9),(7,9),(8,10),(9,10),(10,11),(11,12)]

cur.executemany('INSERT INTO produts_categories (product_id,category_id) VALUES (?,?)', new_products_categories)

cur.execute('''CREATE TABLE IF NOT EXISTS pictures (
    id INTEGER PRIMARY KEY,
    filepath TEXT NOT NULL,
    product_id INTEGER REFERENCES product(id)
)''')

pictures_location = 'Gymnasiearbete\my_server\static\images'

new_pictures = [
    ('static/images/p1i1.jpg',1),
    ('static/images/p1i2.jpg',1),
    ('static/images/p1i3.jpg',1),
    ('static/images/p2i1.jpg',2),
    ('static/images/p2i2.jpg',2),
    ('static/images/p2i3.jpg',2),
    ('my_server\static\imagesp3i1.jpg',3),
    ('my_server\static\imagesp3i2.jpg',3),
    ('my_server\static\imagesp3i3.jpg',3)
    ]

cur.executemany('INSERT INTO pictures (filepath,product_id) VALUES (?,?)', new_pictures)

#Ta bort?
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
    password TEXT NOT NULL,
    admin INTEGER NOT NULL
)''')

new_users = [('admin','admin','admin@gmail.com',b'$2b$12$mGSFnbjslxrgz2T18N2YQuQEo3aiTX.sHzkptZLfLxpygg81E7v8C',1)]

cur.executemany('INSERT INTO users (name,username,email,password,admin) VALUES (?,?,?,?,?)', new_users)

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
