from program import app

@app.route('/')
@app.route('/index')
# Funtionnames gleich der Route: Best Practice
def index():
    return 'Hello Word!'
