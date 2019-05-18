from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    # this action go to face detection page
    return render_template('face.html')

@app.route('/store')
def store_face():
    # store face
    pass

@app.route('/search')
def search_face():
    # search face in storage
    pass