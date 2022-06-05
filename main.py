import sys
sys.path.insert(0,"./src")
from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    lang = request.args.get('lang')
    return render_template("home.html", lang=lang)

@app.route('/api')
def api():
    lista = {}
    lista["x1"] = request.args.get('x1')
    lista["y1"] = request.args.get('y1')
    lista["x2"] = request.args.get('x2')
    lista["y2"] = request.args.get('y2')

    return make_response(jsonify(lista))


if __name__ == "__main__":
    app.run(debug=True)


