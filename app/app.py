import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///data/skillsift.db")

@app.after_request
def after_request(response):
    # Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


# TODO: create /save_location route in order to store a users location data -
# longitude & latitude - gathered from the geolocation API

# @app.route("/search", methods=["GET", "POST"])
# def search():

if __name__ == "__main__":
    app.run(debug=True)
