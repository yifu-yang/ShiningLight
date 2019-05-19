from flask import Flask,render_template,json,request

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    # this action go to face detection page
    return render_template('face.html')

@app.route('/store',methods=['POST'])
def store_face():
    # store face
    return request.form['img']

@app.route('/search',methods=['POST'])
def search_face():
    # search face in storage
    pass