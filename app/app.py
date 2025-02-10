import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, jsonify

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
# displays a list of all skills found and how many times they appear


# TODO: create 'Charts' route
# page with different charts displaying frequency of tech keywords found


# TODO: finish filling out scrape route
@app.route("/scrape", methods=["POST"])
def scrape_jobs():
    # get from data from manual input
    job_title = request.form.get("job_title")
    location = request.form.get("location")
    
    # run web scraper (scrapy)
    keywords = scrape_job_postings(job_title, location, limit=100)
    
    # return results to the client for storage
    return jsonify({
        # other data needed? just keywords data needed?
        "location": location,
        "keywords": keywords
    })


# def scrape_job_postings(lob_title, location, limit):
    # placeholder for web scraping logic
    # return ["keyword1", "keyword2", "keyword3"]


if __name__ == "__main__":
    app.run(debug=True)
