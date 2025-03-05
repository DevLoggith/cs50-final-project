import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, jsonify
from scrape import scrape_website

load_dotenv()

app = Flask(__name__)

@app.after_request
def after_request(response):
    # Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    # retrieve env variables and pass to font end
    nominatim_user_agent = os.getenv("NOMINATIM_USER_AGENT")
    return render_template("index.html", nominatim_user_agent=nominatim_user_agent)


# TODO: create 'List' route
# displays a list of ALL skills found and how many times they appear


# TODO: create 'Charts' route
# page with different charts displaying frequency of tech keywords found
# limited to the top 5-10 tech keywords returned


# TODO: finish filling out scrape route
@app.route("/scrape", methods=["POST"])
def scrape_jobs():
    # get from data from manual input
    job_title = request.form.get("job_title")
    location = request.form.get("location")
    
    # run web scraper (selenium in scrape.py)
    keywords = scrape_website(job_title, location, limit=100)
    
    # return results to the client for storage
    return jsonify({
        # other data needed? just keywords data needed?
        "location": location,
        "job_title": job_title,
        "keywords": keywords
    })


if __name__ == "__main__":
    app.run(debug=True)
