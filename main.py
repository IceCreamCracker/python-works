import sys
sys.path.insert(0,"./src")

from functions import *
from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
#import json


rectList = []

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    global rectList
    return render_template("home.html", rectList=rectList)

@app.route('/api')
def api():
    global rectList
    rect = Rect(
            int(request.args.get('x1')),
            int(request.args.get('y1')),
            int(request.args.get('x2')),
            int(request.args.get('y2'))
            )
    rectList = getNewRectList(rectList,rect)    
    rectListForJson = [rect.__dict__ for rect in rectList]
    return make_response(jsonify(rectListForJson))

#sim é só digitar /delete na frente da url e pronto. Super seguro
@app.route('/delete')
def delete():
    global rectList
    rectList = []
    return make_response(jsonify({"deleted":True}))

if __name__ == "__main__":
    app.run(debug=True)


