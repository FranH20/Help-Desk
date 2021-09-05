from app import *
from flask import Flask,render_template

@app.route('/profile')
def profile():
    lista=[]
    if 'emailuser' in session:
        #return 'You are logged in as ' + session['emailuser']
        user_collection=mongo.db.user
        login_user=user_collection.find_one({'emailuser':session['emailuser']})
        for v in login_user.values():
            lista.append(v)
        return render_template('profile.html',datos=login_user)
    return render_template('login.html')

@app.route('/sesiondestroy')
def sessiondestroy():
    session.clear()
    return render_template('login.html')

@app.route('/login')
def entrarlogin():
    if 'emailuser' in session:
        return redirect(url_for('profile'))
    return render_template('login.html')

@app.route('/verificar', methods=['POST'])
def login():
    user_collection = mongo.db.user
    login_user = user_collection.find_one({'emailuser': request.form['emailuser']})
    if login_user is None:
        flash('EMAIL INCORRECTO')
        return render_template('login.html')
    else:    
        session['username']=login_user['username']
        if login_user:
            hashpass = login_user['password']


            if bcrypt.checkpw(request.form['passworduser'].encode('utf-8'), hashpass):
                session['emailuser'] = request.form['emailuser']
                return redirect(url_for('profile'))

        flash('PASSWORD INCORRECTA')
        return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        if request.form['password']==request.form['passworddos']:
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
                return redirect(url_for('profile'))
            else:
                flash('El email ya se ha registrado')
                return render_template('register.html')
        else:
            flash('LA PASSWORD NO COINCIDE')
            return render_template('register.html')
    else:
        return render_template('register.html')
