from flask import Flask,render_template
app = Flask(__name__)

@app.route("/home")
def hello_world():
    return render_template("home.html")

@app.route("/import")
def import_page():
    return render_template("import.html")

@app.route("/export")
def export_page():
    return render_template("export.html")

if __name__ == "__main__":
    app.run()
    