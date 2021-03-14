from my_server import db
from my_server.models import Product

for product in Product.query.all():
    product.description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vel ullamcorper metus, id imperdiet urna. Sed semper lorem risus, sit amet tincidunt quam consequat quis. Mauris lectus nulla, euismod ac sem eget, volutpat lobortis massa. Integer imperdiet feugiat nisl eget iaculis. Sed commodo vitae felis ultrices facilisis. Mauris at malesuada eros, sit amet tincidunt arcu. Ut vehicula elit a imperdiet scelerisque. Sed sed odio sit amet felis porta scelerisque in eget turpis. Morbi venenatis nisl ac magna varius, aliquam bibendum mi cursus. Cras felis libero, mattis et fringilla non, blandit ac nisi. Sed ante justo, facilisis porttitor rutrum eu, pellentesque id mi. Vestibulum et mauris sit amet felis tristique mattis. '


db.session.commit