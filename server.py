from flask import Flask,render_template,request,jsonify,make_response
import json

app = Flask(__name__)

@app.route('/')
def welccome():
    return 'welcome to our flask web app'

@app.route("/home")
def hello_world():
    return render_template("home.html")

@app.route("/import")
def import_page():
    return render_template("import.html")

@app.route("/export")
def export_page():
    with open('static/data/data.json') as f:
        cities = json.load(f)
    return render_template("export.html",cities=cities)

@app.route('/readJson', methods=['GET','POST'])
def read_json():
    if request.method == 'POST':
        return "Nothing to post yet"
    else:
        with open('static/data/data.json') as f:
            cities = json.load(f)
        res = make_response(jsonify(cities),200)
        return res

if __name__ == "__main__":
    app.run(debug = True)
    