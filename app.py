from flask import Flask, render_template, url_for, request, session, redirect
#from flask_pymongo import PyMongo

app = Flask(__name__)

#app.config['MONGO_DBNAME'] = 'helpdesk'
#app.config['MONGO_URI'] = 'mongodb+srv://test:test@episupt-tasga.gcp.mongodb.net/test?retryWrites=true&w=majority'
#mongo = PyMongo(app)
app = Flask(__name__)


from login import *
#@app.route('/')
#def index():
 #   return render_template('index.html')


if __name__ == '__main__':
    app.run()
