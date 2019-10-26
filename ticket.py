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
        estado="abierto"
        user_collection.insert(
            {'username': username, 'emailuser': emailuser, 'tema': tema, 'emailuser': emailuser
                , 'asunto': asunto, 'descripcion': descripcion,'prioridad':prioridad,'estado':estado})
    return createticket()