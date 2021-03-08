from my_server import db
from my_server.models import Product
from random import randint, uniform

for product in Product.query.all():
    if product.category == 2:
        product.stock = int(product.stock * uniform(0.2,5.0))
        product.price = randint(100,200)*product.price
        db.session.commit()

