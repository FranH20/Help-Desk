from flask import Flask,render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MONGO_DBNAME'] = 'helpdesk'
app.config['MONGO_URI'] = 'mongodb://localhost/helpdesk'

mongo = PyMongo(app)

from login import *
from profile import *
from ticket import *
from admin import *
from ticketadmin import *
from incidencias import *
from usuarioincidencia import*

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
