import sys
sys.path.insert(0,"./src")

import json
import time
from functions import *
from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
#import json


rectList = []

app = Flask(__name__)
CORS(app) #da acesso a api de todas as origens, sem isso dá erro
#rota principal, retorna página home
@app.route('/')
def home():
    return render_template("home.html")

#esta rota é para as requisições de retangulos processadas pelo backend
@app.route('/api')
def api():
    time.sleep(0.1)
    global rectList
    rect = Rect(
            int(request.args.get('x1')),
            int(request.args.get('y1')),
            int(request.args.get('x2')),
            int(request.args.get('y2'))
            )
    #rectList = json.load(request.args.get('rectList'))#loada o json
    rectList = getNewRectList(rectList,rect)    
    rectListForJson = [rect.__dict__ for rect in rectList] #transforma rectList em dicionário para ser transformada em json
    time.sleep(0.1)
    return make_response(jsonify(rectListForJson))

#sim é só digitar /delete na frente da url e pronto. Super seguro
#requisição GET para deletar a lista de retângulos
@app.route('/delete')
def delete():
    global rectList
    rectList = []
    return make_response(jsonify({"deleted":True}))

#boilerplate
if __name__ == "__main__":
    app.run()


