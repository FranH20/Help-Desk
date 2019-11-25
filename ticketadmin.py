from app import *

@app.route('/ticketadmin')
def ticketadmin():
	ticket_collection=mongo.db.ticket
	asunto_collection=mongo.db.asunto
	lista_tickets=ticket_collection.find()
	lista_asunto=asunto_collection.find()
	return render_template('ticketadmin.html',tickets=lista_tickets,asuntos=lista_asunto)

@app.route('/ticketselect/<numero>',methods=['POST','GET'])
def ticketselect(numero):
	ticket_collection=mongo.db.ticket
	tema_collection=mongo.db.temas
	lista_tickets=ticket_collection.find_one({'numero':numero})
	lista_tema=tema_collection.find()
	return render_template('ticketselect.html',ticket=lista_tickets,temas=lista_tema)

@app.route('/ticketreply',methods=['POST'])
def ticketreply():
	ticketxreply_collection=mongo.db.ticketxreply
	admin_collection=mongo.db.admin
	ticket_collection=mongo.db.ticket
	user_find=admin_collection.find_one({'emailadmin':"jose@jose.com"})
	idadmin=user_find['_id']
	tipoadmin=user_find['adminroll']
	respuestafecha=datetime.datetime.today()
	estado=request.form['estado']
	descripcion=request.form['descripcion']
	idticket=request.form['idticket']
	archivo = request.files['archivo']
	mongo.save_file(archivo.filename, archivo)
	ticketxreply_collection.insert({'idticket':idticket,'id_admin':idadmin,'tipo_admin':tipoadmin,'reply_date':respuestafecha,'estado':estado,'descripcion':descripcion,'archivo':archivo.filename})
	ticket_id=ticket_collection.find_one({'_id':idticket})
	if ticket_id['asignado'] is None:
		ticket_collection.find_one_and_update({"_id" : idticket},{"$set":{"asignado": idadmin}},upsert=True)
	return ticketadmin()