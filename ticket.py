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
                , 'asunto': asunto, 'descripcion': descripcion,'archivo':archivo.filename,'prioridad':prioridad,'estado':estado,'fecha_creacion':fecha})
    return createticket()

@app.route('/ticketespera')
def cargarticketespera():
    ticket_collection=mongo.db.ticket
    tema_collection=mongo.db.temas
    lista_temas=tema_collection.find()
    ticket_all = ticket_collection.find({'emailuser': session['emailuser'],'estado':"A"})
    return render_template('ticketespera.html',datos=ticket_all,temas=lista_temas)

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)