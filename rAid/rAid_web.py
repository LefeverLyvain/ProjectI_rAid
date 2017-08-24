from flask import Flask, render_template
from rAid_DbClass import DbClass

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/info')
def info():
    DbLayer = DbClass()
    result = DbLayer.getDataFromDatabase()
    return render_template("info.html", titel=result)

if __name__ == '__main__':
    app.run(debug=True)
