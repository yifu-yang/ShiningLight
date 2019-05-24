from flask import Flask,render_template,json,request
import base64
import uuid
import  demjson
import  face_comm
import  face_handler
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.debug = True

@app.route('/')
def index():
    # this action go to face detection page
    return render_template('face.html')

@app.route('/store',methods=['POST'])
def store_face():
    # store face
    retData={'code':0}
    imgdata = request.form['img'].split(',',1)[1]
    username = request.form['username']
    imgdata = base64.urlsafe_b64decode(imgdata)
    filename = './imgs/'+str(uuid.uuid4())+'.png'  
    with open(filename, 'ab') as f:
        f.write(imgdata)
    if face_handler.add_face_index(username,filename):
        retData['data']={'succ':1}
    else:
        retData['data']={'succ':0}
    return str(retData)

@app.route('/search',methods=['POST'])
def search_face():
    # search face in storage
    retData={'code':0}
    imgdata = base64.urlsafe_b64decode(request.form['img'].split(',',1)[1])
    filename = './imgs/'+str(uuid.uuid4())+'.png'  
    with open(filename, 'ab') as f:
        f.write(imgdata)
    retData['data'] = face_handler.query_face(filename)
    return str(retData)