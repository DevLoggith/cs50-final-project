import os
from flask import Flask, redirect, render_template, request, jsonify

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
    return render_template("index.html")

# TODO: create 'List' route
# displays a list of all skills found and how many times they appear

# TODO: create 'Charts' route
# page with different charts displaying frequency of tech keywords found

# TODO: create scrape route
@app.route('/scrape', methods=['POST'])
def scrape_jobs():
    # receive JSON data from sendLocationToServer function
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    # get from data from manual input
    job_title = request.form.get('job_title')
    manual_location = request.form.get('location')

    # determine which method of location input to use
    if latitude and longitude:
        coords = f"{latitude}, {longitude}" # TODO: what format to pass to 'geocode'
        location = geocode(coords)
    elif manual_location:
        location = manual_location
    else:
        return jsonify({"error": "No location data provided"}), 400
    
    # run web scraper (scrapy)
    keywords = scrape_job_postings(job_title, location, limit=100)
    
    # return results to the client for storage
    return jsonify({
        "location": location,
        "keywords": keywords
    })

# def scrape_job_postings(lob_title, location, limit):
    # placeholder for web scraping logic
    # return ["keyword1", "keyword2", "keyword3"]

# def geocode(location):
    # placeholder for geocoding logic (convert to human readable address)
    # return "Cleveland, OH", or "44107"

if __name__ == "__main__":
    app.run(debug=True)
