from app import *

@app.route('/generarticket',methods=['POST'])
def generarticket():
    user_collection = mongo.db.ticket
    fecha=datetime.datetime.today()
    if request.method == 'POST':
        contador=request.form.get('contador')
        asunto=request.form.get('asunto')
        username = request.form.get('username')
        emailuser = request.form.get('emailuser')
        tema = request.form.get('tema')
        asunto = request.form.get('asunto')
        descripcion = request.form.get('descripcion')
        prioridad=request.form.get('prioridad')
        archivo = request.files['archivo']
        mongo.save_file(archivo.filename, archivo)
        estado="A"
        user_collection.insert(
            {'numero':contador,'username': username, 'emailuser': emailuser, 'tema': tema, 'emailuser': emailuser
                , 'asunto': asunto, 'descripcion': descripcion,'archivo':archivo.filename,'prioridad':prioridad,'estado':estado,'fecha_creacion':fecha,'asignado':"Ninguno"})
    return createticket()

@app.route('/ticketespera')
def cargarticketespera():
    ticket_collection=mongo.db.ticket
    tema_collection=mongo.db.temas
    asunto_collection=mongo.db.asunto
    lista_temas=tema_collection.find()
    ticket_all = ticket_collection.find({'emailuser': session['emailuser'],'estado':"A"})
    #
    lista_tickets=ticket_collection.find()
    lista_asunto=asunto_collection.find()
    return render_template('ticketespera.html',tickets=ticket_all,asuntos=lista_asunto)
    #return render_template('ticketespera.html',datos=ticket_all,temas=lista_temas)

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

@app.route('/ticketselectuser/<numero>/<id>',methods=['POST','GET'])
def ticketselectuser(numero,id):
    ticket_collection=mongo.db.ticket
    tema_collection=mongo.db.temas
    admin_collection=mongo.db.admin
    #ticket_collection.update_one({'numero':numero},{"$set":{"asignado":idadmin}})#NUEVA PARTE
    #list_admin=ticket_collection.find_one({'emailadmin':session['emailadmin']})#NUEVA PARTE
    #idadmin=list_admin['_id']#NUEVO
    #ticket_collection.update_one({'numero':numero},{"$set":{"asignado":idadmin}})#NUEVA PARTE
    lista_tickets=ticket_collection.find_one({'numero':numero})
    lista_tema=tema_collection.find()
    hilo_ticket=mongo.db.ticketxreply
    hilo_list=hilo_ticket.find({'idticket':id})
    idadmin=lista_tickets['asignado']
    list_user=admin_collection.find_one({'_id':idadmin})
    return render_template('ticketselectuser.html',ticket=lista_tickets,temas=lista_tema,listhilo=hilo_list,usuarios=list_user)


@app.route('/ticketreplyuser',methods=['POST'])
def ticketreplyuser():
    ticketxreply_collection=mongo.db.ticketxreply
    admin_collection=mongo.db.admin
    user_collection=mongo.db.admin
    ticket_collection=mongo.db.ticket
    user_find=user_collection.find_one({'emailuser':session['emailuser']})
    idadmin=session['emailuser']
    tipoadmin="user"
    respuestafecha=datetime.datetime.today()
    estado=request.form['estado']
    descripcion=request.form['descripcion']
    idticket=request.form['idticket']
    numeroticket=request.form['numero']
    archivo = request.files['archivo']
    mongo.save_file(archivo.filename, archivo)
    ticketxreply_collection.insert({'idticket':idticket,'id_admin':idadmin,'tipo_admin':tipoadmin,'reply_date':respuestafecha,'estado':estado,'descripcion':descripcion,'archivo':archivo.filename})    
    ticket_collection.update_one({'numero':numeroticket},{"$set":{"estado":estado}})#NUEVA PARTE
    return cargarticketespera()

@app.route('/ticketcerrado')
def cargarticketcerrado():
    ticket_collection=mongo.db.ticket
    tema_collection=mongo.db.temas
    asunto_collection=mongo.db.asunto
    lista_temas=tema_collection.find()
    ticket_all = ticket_collection.find({'emailuser': session['emailuser'],'estado':"C"})
    #
    lista_tickets=ticket_collection.find()
    lista_asunto=asunto_collection.find()
    return render_template('ticketcerrado.html',tickets=ticket_all,asuntos=lista_asunto)

@app.route('/ticketselectcerrado/<numero>/<id>',methods=['POST','GET'])
def ticketselectcerrado(numero,id):
    ticket_collection=mongo.db.ticket
    tema_collection=mongo.db.temas
    admin_collection=mongo.db.admin
    lista_tickets=ticket_collection.find_one({'numero':numero})
    lista_tema=tema_collection.find()
    hilo_ticket=mongo.db.ticketxreply
    hilo_list=hilo_ticket.find({'idticket':id})
    idadmin=lista_tickets['asignado']
    list_user=admin_collection.find_one({'_id':idadmin})
    return render_template('ticketselectcerrado.html',ticket=lista_tickets,temas=lista_tema,listhilo=hilo_list,usuarios=list_user)