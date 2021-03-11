from flask import redirect, url_for, request, Blueprint, flash
from flask import render_template as rt
from my_server.admin.utils import admin_required, send_newsletter
from my_server.models import Product, Picture, Newsletter_Recipients, User, Category
from werkzeug.utils import secure_filename
import os
from my_server import db,app

admin = Blueprint('admin',__name__)

@admin.route('/admin')
#@admin_required
def admin_home():
    return rt('admin.html',categories = Category.query.filter(Category.name!='Main').all())

@admin.route('/admin/category')
def admin_category():
    id = request.args['category_id']
    return rt('admin_products.html',products=Product.query.filter_by(category=id).all())


@admin.route('/admin/send_email', methods=['GET','POST'])
@admin_required
def send_email():
    if request.method == 'POST':
        subject = request.form['subject']
        content = request.form['content']
        newsletter = request.form.getlist('newsletter')
        general = request.form.getlist('general')
        recipients = []
        if newsletter != []:
            for recipient in Newsletter_Recipients.query.all():
                recipients.append(recipient.email)
        if general != []:
            for recipient in User.query.all():
                recipients.append(recipient.email)
        if recipients == []:
            flash('något gick fel, försök igen','warning')
            return rt('send_email.html')
        send_newsletter(subject,content,recipients)
    return rt('send_email.html')

@admin.route('/admin/edit', methods=['GET','POST'])
#@admin_required
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
    
    pictures = Picture.query.filter_by(product_id=product_id).all()
    return rt('edit_product.html',product = product, pictures=pictures)

@admin.route('/admin/edit/upload_picture', methods=['POST'])
def upload_picture():
    product_id = request.form['id']
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    picture = Picture(product_id=product_id,filepath=f'static/images/{filename}')
    db.session.add(picture)
    db.session.commit()
    return redirect(url_for('admin.admin_edit',product_id=product_id))



@admin.route('/admin/add')
@admin_required
def admin_add():
    return redirect(url_for('admin.admin_home'))