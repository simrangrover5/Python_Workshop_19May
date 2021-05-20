from logging import debug
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")  # / --> host/domain , localhost
def home():
    # return "hello world"
    return render_template("index.html")

@app.route("/getmovie/", methods=['POST', 'GET'])
def getmovie():
    if request.method == "POST":
        movie = request.form.get("movie")
        key = "508330f0"
        url = f"http://www.omdbapi.com/?apikey={key}&t={movie}"
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            values = ['Title', 'Year', 'Runtime', 'Genre', 'Director', 'imdbRating', 'Type', 'BoxOffice', 'Language',
            'Plot', 'Actors']
            temp = {}
            for val in values:
                temp[val] = data.get(val)
            img = data.get("Poster")
            return render_template("data.html", val=temp, poster=img)
        else:
            return "INVALID URL"
    else:
        return render_template("index.html")

app.run(host="localhost", port=80, debug=True)