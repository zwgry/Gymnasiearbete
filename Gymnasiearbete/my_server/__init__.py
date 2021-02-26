from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import os



app = Flask(__name__)
mail = Mail(app)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECURITY_PASSWORD_SALT'] = os.urandom(16)
app.config['MAIL_DEFAULT_SENDER'] = 'mathiaswistrom02@gmail.com'
app.config['MAIL_USERNAME'] = os.environ['EMAIL']
app.config['MAIL_PASSWORD'] = os.environ['EMAIL_PASSWORD']

db = SQLAlchemy(app)

from my_server.models import Product, Picture

from my_server.main.routes import main
from my_server.shop.routes import shop
from my_server.admin.routes import admin
from my_server.users.routes import users

app.register_blueprint(main)
app.register_blueprint(shop)
app.register_blueprint(admin)
app.register_blueprint(users)
