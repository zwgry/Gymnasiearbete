from flask import redirect, url_for, Blueprint
from flask import render_template as rt
from my_server.admin.utils import admin_required, sql_request, sql_request_prepared, insert_user

admin = Blueprint('admin',__name__)

@admin.route('/admin')
@admin_required
def admin_home():
    return rt('admin.html',products = sql_request('SELECT * FROM products'))

@admin.route('/admin/edit/<id>')
@admin_required
def admin_edit(id = None):
    if id == None:
        return redirect(url_for('admin.admin_home'))
    product = sql_request_prepared('SELECT * FROM products WHERE id = ?',(id,))
    return rt('edit_product.html',product = product)

@admin.route('/admin/add')
@admin_required
def admin_add():
    return redirect(url_for('admin.admin_home'))