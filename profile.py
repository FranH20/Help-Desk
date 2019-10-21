from app import *

@app.route('/dashboarduser')
def dashboarduser():
    return render_template('userbase.html')

@app.route('/createticket')
def createticket():
    return render_template('createticket.html')