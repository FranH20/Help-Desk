from app import *


@app.route('/admin')
def admin():
    if 'emailuser' in session:
        return redirect(url_for('profile'))
    else:
        if 'adminroll' in session:
            return render_template('usuarios.html')
        # TODO REVISAR PORQUE NO SIRVE EL URL FOR
        else:
            return render_template('loginadmin.html')


@app.route('/verificaradmin', methods=['POST'])
def loginadmin():
    admin_collection = mongo.db.admin
    login_admin = admin_collection.find_one({'emailadmin': request.form['emailadmin']})
    if login_admin is None:
        flash('EMAIL INCORRECTO')
        return render_template('loginadmin.html')
    else:
        session['adminroll'] = login_admin['adminroll']
        if login_admin:
            if request.form['passwordadmin'] == login_admin['password']:
                session['emailadmin'] = request.form['emailadmin']
                return render_template('usuarios.html')
                # TODO CAMBIAR POR URL FOR PARA LA URL PERO SI SIRVE EL LOGIN

        flash('CONTRASEÑA INCORRECTA')
        return render_template('loginadmin.html')


@app.route('/usuarios')
def usuario():
	admin_collection = mongo.db.admin
	roles_collection=mongo.db.roll
	temas_collection=mongo.db.temas
	admin_usuarios = admin_collection.find()
	roles=roles_collection.find()
	temasc=temas_collection.find()
	return render_template('usuarios.html',usuarios=admin_usuarios,rolls=roles,temas=temasc,rolldos=roles)


