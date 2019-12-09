from app import *

@app.route('/dashboarduser')
def dashboarduser():
    return render_template('userbase.html')

@app.route('/createticket')
def createticket():
	user_collection = mongo.db.ticket
	theme_collection=mongo.db.temas
	asunto_collection=mongo.db.asunto
	lista_asunto=asunto_collection.find()
	lista_temas=theme_collection.find()
	contador=user_collection.count_documents({})
	contador=contador+1
	lista = []
	lista.append(session['emailuser'])
	lista.append(session['username'])
	return render_template('createticket.html',emailuser=lista[0],username=lista[1],contador=contador,temas=lista_temas,asuntos=lista_asunto)