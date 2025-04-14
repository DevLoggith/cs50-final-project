import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, session
import secrets
from scrape import scrape_job_descriptions
from extract import extract_total_keywords

load_dotenv()

app = Flask(__name__)
# generates a new session key each time the program is run
app.secret_key = secrets.token_hex(16)

@app.after_request
def after_request(response):
    # Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    # retrieve env variables and pass to font end JS
    nominatim_user_agent = os.getenv("NOMINATIM_USER_AGENT")
    return render_template("index.html", nominatim_user_agent=nominatim_user_agent)


# TODO: finish 'List' route
# displays a list of ALL skills found and how many times they appear
@app.route("/list")
def list():
    # rows = keywords_dict

    return render_template("list.html")


# TODO: create 'Charts' route
# page with different charts displaying frequency of tech keywords found
# limited to the top 5-10 tech keywords returned?


@app.route("/scrape", methods=["POST"])
def scrape_jobs():
    # TODO: add form validation
    job_title = request.form.get("job_title")
    location = request.form.get("location")
    
    job_descriptions = scrape_job_descriptions(job_title, location, limit=10)
    keywords_dict = extract_total_keywords(job_descriptions)
    session["keywords_data"] = keywords_dict
    session_data = session["keywords_data"]
    return render_template("list.html", session_data=session_data)


if __name__ == "__main__":
    app.run(debug=True)
