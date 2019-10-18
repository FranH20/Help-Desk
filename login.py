from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt
import codecs

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MONGO_DBNAME'] = 'helpdesk'
app.config['MONGO_URI'] = 'mongodb+srv://test:test@episupt-tasga.gcp.mongodb.net/helpdesk?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def index():
    if 'emailuser' in session:
        return 'You are logged in as ' + session['emailuser']

    return render_template('index.html')

@app.route('/login')
def entrarlogin():
    return render_template('login.html')

@app.route('/verificar', methods=['POST'])
def login():
    user_collection = mongo.db.user
    login_user = user_collection.find_one({'emailuser': request.form['emailuser']})

    if login_user:
        hashpass = login_user['password']


        if bcrypt.checkpw(request.form['passworduser'].encode('utf-8'), hashpass):
            session['emailuser'] = request.form['emailuser']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user_collection = mongo.db.user
        existing_user = user_collection.find_one({'emailuser': request.form['emailuser']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            username = request.form.get('username')
            emailuser = request.form.get('emailuser')
            genderuser = request.form.get('genderuser')
            user_collection.insert(
                {'firstname': firstname, 'lastname': lastname, 'username': username, 'emailuser': emailuser
                    , 'genderuser': genderuser, 'password': hashpass})
            session['emailuser'] = request.form['emailuser']
            return redirect(url_for('index'))

        return 'That email already exists!'

    return render_template('register.html')


if __name__ == '__main__':
    app.debug = True
    app.run()