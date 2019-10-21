from flask import Flask, render_template, url_for, request, session, redirect,flash
from flask_pymongo import PyMongo


app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MONGO_DBNAME'] = 'helpdesk'
app.config['MONGO_URI'] = 'mongodb+srv://test:test@episupt-tasga.gcp.mongodb.net/helpdesk?retryWrites=true&w=majority'

mongo = PyMongo(app)


from login import *
from profile import *


#@app.route('/')
#def index():
 #   return render_template('index.html')


if __name__ == '__main__':
    app.run()
