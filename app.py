
from flask import Flask, jsonify, request, abort, render_template, redirect, url_for
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/novedades")
def novedades():
    return render_template("novedades.html")


@app.route("/colecciones")
def colecciones():
    return render_template("colecciones.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
