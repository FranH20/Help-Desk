from app import *

@app.route('/dashboarduser')
def dashboarduser():
    return render_template('userbase.html')

@app.route('/createticket')
def createticket():
    lista = []
    lista.append(session['emailuser'])
    lista.append(session['username'])
    return render_template('createticket.html',emailuser=lista[0],username=lista[1])