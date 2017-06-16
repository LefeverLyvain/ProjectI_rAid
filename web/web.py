import os

from flask import Flask, render_template
from DbClass import DbClass

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")

# @app.route('/collection')
# def collection():
#     DbLayer = DbClass()
#     listGames = DbLayer.getcollection()
#     return render_template("collection.html",games=listGames)
#
# @app.route('/collection/<gameName>')
# def gamedetails(gameName):
#     DbLayer = DbClass()
#     result = DbLayer.getgame(gameName)
#     return render_template('gamedetails.html',game=result)
#
#     from flask import abort
#     abort(404)

# @app.route('/about')
# def contact():
#     return render_template("about.html")

@app.errorhandler(404)
def pageNotFound(error):
    return render_template("error.html", error=error)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    host = "0.0.0.0"
    app.run(host=host, port=port, debug=True)

