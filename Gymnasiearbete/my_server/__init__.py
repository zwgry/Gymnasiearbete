from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

from my_server.main.routes import main
from my_server.shop.routes import shop
from my_server.admin.routes import admin
from my_server.users.routes import users

app.register_blueprint(main)
app.register_blueprint(shop)
app.register_blueprint(admin)
app.register_blueprint(users)
