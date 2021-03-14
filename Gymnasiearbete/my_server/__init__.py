from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import os


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['UPLOAD_FOLDER'] = 'my_server/static/images/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECURITY_PASSWORD_SALT'] = os.urandom(16)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'testmailgyar@gmail.com' #mail till verifikationsmail och för nyhetsbrev
app.config['MAIL_PASSWORD'] = 'gyar2020' #lösenord till mailen
mail = Mail(app)
db = SQLAlchemy(app)

from my_server.models import Product, Picture

from my_server.main.routes import main
from my_server.shop.routes import shop
from my_server.admin.routes import admin
from my_server.users.routes import users
from my_server.error.routes import errors

app.register_blueprint(main)
app.register_blueprint(shop)
app.register_blueprint(admin)
app.register_blueprint(users)
app.register_blueprint(errors)
