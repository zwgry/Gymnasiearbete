from flask import Flask


app = Flask(__name__)
app.secret_key = 'aaoaao'
from my_server import routes
#from my_server import errors