from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

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
