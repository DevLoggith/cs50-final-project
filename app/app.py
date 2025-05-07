import os
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, session
from functools import wraps
import secrets
from scrape import scrape_job_descriptions
from extract import extract_total_keywords

load_dotenv()

app = Flask(__name__)
# generates a new session key each time the program is run
app.config["SECRET_KEY"] = secrets.token_hex(16)

@app.after_request
def after_request(response):
    # Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

def check_for_data(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "keywords_data" not in session or session["keywords_data"] == None:
            flash("Please run a search first to generate data", "error")
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    # retrieve env variables and pass to font end JS
    nominatim_user_agent = os.getenv("NOMINATIM_USER_AGENT")
    return render_template("index.html", nominatim_user_agent=nominatim_user_agent)


@app.route("/list", methods=["GET"])
@check_for_data
def list():
    session_data = session["keywords_data"]
    sorted_keywords_dict = dict(sorted(session_data.items(), key=lambda item: item[1], reverse=True))
    return render_template("list.html", sorted_keywords_dict=sorted_keywords_dict)


@app.route("/charts")
@check_for_data
def charts():
    data = session["keywords_data"]
    chart_data = []
    for tech, count in data.items():
        chart_data.append([tech, count])
    

    return render_template("charts.html", chart_data=chart_data)


# TODO: create 'About' route


@app.route("/scrape", methods=["POST"])
def scrape_jobs():
    job_title = request.form.get("job_title")
    location = request.form.get("location")

    if not job_title:
        flash("Please enter a job title")
        return redirect("/")
    
    if not location:
        flash("Please enter a location")
        return redirect("/")
    
    job_descriptions = scrape_job_descriptions(job_title, location, limit=50)
    if job_descriptions == []:
        return render_template("no-results.html")
    else:
        keywords_dict = extract_total_keywords(job_descriptions)

    session["keywords_data"] = keywords_dict
    session_data = session["keywords_data"]
    sorted_keywords_dict = dict(sorted(session_data.items(), key=lambda item: item[1], reverse=True))
    return render_template("list.html", sorted_keywords_dict=sorted_keywords_dict)


if __name__ == "__main__":
    app.run(debug=True)
