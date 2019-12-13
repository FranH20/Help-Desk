from app import *

@app.route('/incidencias')
def incidencias():
    oficinas_collection=mongo.db.oficina
    problemas_collection=mongo.db.incidenciausuario
    lista_oficina=oficinas_collection.find()
    personal_collection=mongo.db.personal
    lista_personal=personal_collection.find()
    lista_personaldos=personal_collection.find()
    lista_problemas=problemas_collection.find()
    return render_template('incidencias.html',oficinas=lista_oficina,personal=lista_personal,personaldos=lista_personaldos,problemas=lista_problemas)

@app.route('/guardarincidencia',methods=['POST','GET'])
def guardarincidencia():
    incidenciausuario_collection=mongo.db.incidenciausuario
    idusuario=request.form['idusu']
    elemento=request.form['elemento']
    tipoelemento=request.form['tipoelemento']
    solucion=request.form['solucion']
    problema=request.form['problema']
    fecha=datetime.datetime.today()
    incidenciausuario_collection.insert({'idusuario':idusuario,'elemento':elemento,'tipoelemento':tipoelemento,'solucion':solucion,'problema':problema,'fecha':fecha})
    return redirect(url_for('incidencias'))

@app.route('/usuarioincidencia/<id>',methods=['POST','GET'])
def verusuarioincidencia(id):
    personal_collection=mongo.db.personal
    return render_template('usuarioincidencia.html',personal=id)