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
                return redirect(url_for('usuario'))
                # TODO CAMBIAR POR URL FOR PARA LA URL PERO SI SIRVE EL LOGIN

        flash('CONTRASEÑA INCORRECTA')
        return render_template('loginadmin.html')


@app.route('/usuarios')
def usuario():
    admin_collection = mongo.db.admin
    roles_collection=mongo.db.roll
    temas_collection=mongo.db.temas
    asunto_collection=mongo.db.asunto
    admin_usuarios = admin_collection.find()
    roles=roles_collection.find()
    rolesdos=roles_collection.find()
    temasc=temas_collection.find()
    listasunto=asunto_collection.find()
    return render_template('usuarios.html',usuarios=admin_usuarios,rolls=roles,temas=temasc,rolldos=rolesdos,asuntos=listasunto)

@app.route('/saveuser', methods=['POST'])
def saveroluser():
    firstname=request.form['FirstName']
    lastname=request.form['LastName']
    adminname=request.form['adminname']
    gender=request.form['gender']
    password=request.form['passwordadmin']
    tbroles=request.form['tbroles']
    emailadmin=request.form['emailadmin']
    temp=len(tbroles)
    tbroles=tbroles[:temp-1]# EL CODIGO PARA QUITARLE EL ULTIMO CARACTER AL STRING
    lista=tbroles.split(",")#EL SPLIT QUE CONVERTIRA LA LISTA EN ARRAY
    admin_collection=mongo.db.admin
    admin_collection.insert({'emailadmin':emailadmin,'firstname':firstname,'lastname':lastname,'adminname':adminname,'gender':gender,'adminroll':"B",'password':password,'roles':lista})
    #usuariolist=admin_collection.find_one({'emailadmin':usuario})
    #idusuario=usuariolist['_id']
    #admin_collection.update_one({},{'_id':idusuario},{"$set":{"roles":lista}},multi=True)
    #admin_collection.update_one({'_id':idusuario},{"$set":{"roles":lista}})
    return redirect(url_for('usuario'))
    

@app.route('/savetheme',methods=['POST'])
def savetheme():
    descripcion=request.form['nametema']
    theme_collection=mongo.db.temas
    theme_collection.insert({'descripcion':descripcion})
    return redirect(url_for('usuario'))

@app.route('/saveasunto',methods=['POST'])
def saveasunto():
    nameasunto=request.form['nameasunto']
    asunto_collection=mongo.db.asunto
    asunto_collection.insert({'descripcion':nameasunto})
    return redirect(url_for('usuario'))

@app.route('/saverol',methods=['POST'])
def saverol():
    nombrerol=request.form['namerol']
    tbtemas=request.form['tbtemas']
    temp=len(tbtemas);
    tbtemas=tbtemas[:temp-1]
    listatemas=tbtemas.split(",")
    roles_collection=mongo.db.roll
    roles_collection.insert({'descripcion':nombrerol,'temas':listatemas})
    #listroles=roles_collection.find_one({'descripcion':nombrerol})
    #rol_id=listroles['_id']
    #admin_collection.update_one({'_id':rol_id},{"$set":{"temas":listatemas}})
    return redirect(url_for('usuario'))