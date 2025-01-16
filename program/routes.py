from program import app
from flask import render_template

@app.route('/')
@app.route('/index')
# Funtionnames gleich der Route: Best Practice
def index():
    return render_template("index.html")

@app.route('/100Days') #Keine Dateiendung im Dekorator, das funktioniert hier nicht
# Funtionnames gleich der Route: Best Practice, Keine Zahl am Anfang, daner das "p"
def p100Days():
    return render_template("100Days.html")
