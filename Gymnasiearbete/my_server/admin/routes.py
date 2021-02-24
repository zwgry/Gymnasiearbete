from flask import redirect, url_for, request, Blueprint
from flask import render_template as rt
from my_server.admin.utils import admin_required, sql_request, sql_request_prepared, insert_user
from my_server.models import Product,Picture
from my_server import db

admin = Blueprint('admin',__name__)

@admin.route('/admin')
@admin_required
def admin_home():
    return rt('admin.html',products = Product.query.all())

@admin.route('/admin/edit', methods=['GET','POST'])
@admin_required
def admin_edit():
    if request.method ==  'POST':
        name = request.form['name']
        description = request.form['description']
        stock = request.form['stock']
        product_id = request.form['id']
        product = Product.query.filter_by(id=product_id).first()
        if product.name != name:
            product.name = name
        if product.description != description:
            product.description = description
        if product.stock != stock:
            product.stock = stock    
        db.session.commit()
    elif request.method == 'GET':
        product_id = request.args['product_id']
        if product_id == None:
            return redirect(url_for('admin.admin_home'))
    product = Product.query.filter_by(id=product_id).first()
    
    pictures =Picture.query.filter_by(product_id=product_id).all()
    print(pictures)
    return rt('edit_product.html',product = product, pictures=pictures)

@admin.route('/admin/add')
@admin_required
def admin_add():
    return redirect(url_for('admin.admin_home'))