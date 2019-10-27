from app import *

@app.route('/generarticket',methods=['POST'])
def generarticket():
    user_collection = mongo.db.ticket
    if request.method == 'POST':
        username = request.form.get('username')
        emailuser = request.form.get('emailuser')
        tema = request.form.get('tema')
        asunto = request.form.get('asunto')
        descripcion = request.form.get('descripcion')
        prioridad=request.form.get('prioridad')
        archivo = request.files['archivo']
        mongo.save_file(archivo.filename, archivo)
        estado="abierto"
        user_collection.insert(
            {'username': username, 'emailuser': emailuser, 'tema': tema, 'emailuser': emailuser
                , 'asunto': asunto, 'descripcion': descripcion,'archivo':archivo.filename,'prioridad':prioridad,'estado':estado})
    return createticket()

@app.route('/ticketespera')
def cargarticketespera():
    ticket_collection=mongo.db.ticket
    ticket_all = ticket_collection.find({'emailuser': session['emailuser'],'estado':"abierto"})
    return render_template('ticketespera.html',datos=ticket_all)

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)