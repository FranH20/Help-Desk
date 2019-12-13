from app import *

@app.route('/usuarioincidencia')
def usuarioincidencia():
    return render_template('usuarioincidencia.html')