from flask import redirect, url_for, request, Blueprint
from flask import render_template as rt
from my_server.admin.utils import admin_required, sql_request, sql_request_prepared, insert_user
from my_server.models import Product

admin = Blueprint('admin',__name__)

@admin.route('/admin')
@admin_required
def admin_home():
    return rt('admin.html',products = Product.query.all())

@admin.route('/admin/edit/<id_>', methods=['GET','POST'])
@admin.route('/admin/edit', methods=['POST'])
@admin_required
def admin_edit(id_ = None):
    if request.method ==  'POST':
        name = request.form['name']
        description = request.form['description']
        stock = request.form['stock']
        id_ = request.form['name2']
        print(name,description,stock,id_)
    elif id_ == None:
        return redirect(url_for('admin.admin_home'))
    product = Product.query.filter_by(id=id_).first()
    return rt('edit_product.html',product = product)

@admin.route('/admin/add')
@admin_required
def admin_add():
    return redirect(url_for('admin.admin_home'))