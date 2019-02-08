import flask

app = flask(__name__)



@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')