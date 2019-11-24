from app import *

@app.route('/ticketadmin')
def ticketadmin():
	ticket_collection=mongo.db.ticket
	asunto_collection=mongo.db.asunto
	lista_tickets=ticket_collection.find()
	lista_asunto=asunto_collection.find()
	return render_template('ticketadmin.html',tickets=lista_tickets,asuntos=lista_asunto)