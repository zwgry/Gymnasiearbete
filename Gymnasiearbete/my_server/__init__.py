from flask import Flask


app = Flask(__name__)

from my_server import routes
#from my_server import errors