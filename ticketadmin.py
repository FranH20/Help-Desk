from app import *

@app.route('/ticketadmin')
def ticketadmin():
	ticket_collection=mongo.db.ticket
	asunto_collection=mongo.db.asunto
	lista_tickets=ticket_collection.find()
	lista_asunto=asunto_collection.find()
	#team_info = zip(teams, wins)#NUEVO
	return render_template('ticketadmin.html',tickets=lista_tickets,asuntos=lista_asunto)

@app.route('/ticketselect/<numero>/<id>',methods=['POST','GET'])
def ticketselect(numero,id):
	ticket_collection=mongo.db.ticket
	tema_collection=mongo.db.temas
	admin_collection=mongo.db.admin
	lista_tickets=ticket_collection.find_one({'numero':numero})
	lista_tema=tema_collection.find()
	hilo_ticket=mongo.db.ticketxreply
	hilo_list=hilo_ticket.find({'idticket':id})
	idadmin=lista_tickets['asignado']
	list_user=admin_collection.find_one({'_id':idadmin})
	return render_template('ticketselect.html',ticket=lista_tickets,temas=lista_tema,listhilo=hilo_list,usuarios=list_user)

@app.route('/ticketreply',methods=['POST'])
def ticketreply():
	ticketxreply_collection=mongo.db.ticketxreply
	admin_collection=mongo.db.admin
	ticket_collection=mongo.db.ticket
	user_find=admin_collection.find_one({'emailadmin':session['emailadmin']})
	idadmin=user_find['_id']
	tipoadmin=user_find['adminroll']
	respuestafecha=datetime.datetime.today()
	estado=request.form['estado']
	descripcion=request.form['descripcion']
	idticket=request.form['idticket']
	archivo = request.files['archivo']#El error esta aqui
	mongo.save_file(archivo.filename, archivo)#o aqui
	ticketxreply_collection.insert({'idticket':idticket,'id_admin':idadmin,'tipo_admin':tipoadmin,'reply_date':respuestafecha,'estado':estado,'descripcion':descripcion,'archivo':archivo.filename})# asi que una opcion es quitarla de aqui
	#ticket_id=ticket_collection.find_one({'_id':idticket})
	numero=request.form['numero']
	ticket_collection.update_one({'numero':numero},{"$set":{"asignado":idadmin}})
	ticket_collection.update_one({'numero':numero},{"$set":{"estado":estado}})#NUEVA PARTE
	#if ticket_id['asignado'] is None: #esto esta super mal
		#ticket_collection.find_one_and_update({"_id" : idticket},{"$set":{"asignado": idadmin}},upsert=True)# este query no funciona y crea uno nuevo
	return ticketadmin()