# CS50 Final Project - SkillSift
## Video Demo:  [YouTube link](https://youtu.be/oF-0qjf6SEw)
## Description:
This is my submission for the final project of the CS50x: Intro to Computer
Science course by Harvard. 

Inspired by what I wish would have existed when I was starting my journey into
software engineering, I created SkillSift. It's a web app that takes a users job
title and location then searches their local job boards, returning a list and
graphs of the most requested technologies,  tech skills, and knowledge for their
local market.
### Files:
- **app.py**: Nested inside the "app" folder, this is what's referenced and called
to actually execute the program. Such as `python app.py` from the terminal or
`app:app` when starting deployment with the `CMD` instruction in the Dockerfile.
This file contains the main logic for the  program to run:
    - Handling the templating, rendering, and routing of all the pages of the web
    app
    - Retrieving `env` variables to pass along to the API
    - Getting user data from a form input
    - Calling imported functions to take that user data and perform the search
    - Taking that user data and data returned from the search and storing it in
    a Flask Session to serve to the different rendered pages.
- **scrape.py**: This is the file that contains all the logic to go out and
search the job board and return a list of jobs containing the job title searched
for, and a list of job descriptions matching that job title. That structure looks
like this:

```JSON
[
    {
        "job_title": "",
        "descriptions": 
        [
            {
                "index": 1,
                "description": ""
            },
            {
                "index": 2,
                "description": ""
            }
            ...
        ]
    }
]
```

It incorporates Selenium with Chrome to navigate the page carefully as to not
overload it; filling in and submitting the search form using the user inputted
data passed in via the `"/scrape"` route in `app.py`, navigating those results
and parsing each returned job description, and navigating to subsequent pages if
need be. When each job description is parsed, before it gets added to the jobs
list, it's cleaned to ensure all letters are lowercased, any punctuation or
characters that would not be used in a tech keyword are removed (baring "." like
in ".NET" or "#" in "C#"), and any additional whitespace is also removed. Logging
and error handling is also incorporated to provide progress updates and more
descriptive error messages throughout the runtime of the program.
- **extract.py**: This file contains two functions; the main function that takes
in the jobs list returned in scrape.py and returns a dictionary of keywords and
how many job descriptions each keyword appears in, and a helper function that
finds the relevant keywords in each description and adds them to a Python set.
This assures that each keyword found is only counted once per job description.
When looking through each description to find keywords, it uses the regex library
to target any whitespace or punctuation (specified within the regex pattern)
before and after each word. If an empty jobs list is passed in, an empty dictionary
is returned, the same as if there are no keywords found in any of the descriptions.
- **keywords.py**: This simply contains a Python set  of alphabetized technology
keywords. Imported into extract.py, this is the main list used to compare to words
found in job descriptions.
- **location.js**: One of 2 JavaScript files in the "static" folder (along with
the  2 CSS files), the script only loads and runs when the `index.html` template
is navigated to. This handles:
    - Button functionality used to get a users location from their device(latitude
    & longitude via the [W3C geolocation API](https://www.w3.org/TR/geolocation/))
    - Turning the returned latitude and longitude coordinates into city/state
    location data via the
    [Nominatim reverse geocoding API](https://nominatim.org/release-docs/develop/api/Reverse/)
    - Placing that city/state data into the location field in the `index.html`
    template.
    - Errors such as the user denying permission to use their location, location
    information being unavailable, a timeout, or any other error that could occur
    labeled as "unknown error"
- **charts.js**: Just like `location.js`, this script is only loaded and ran when
a user navigates to the `charts.html` page. This file uses the Google Charts
library and contains the code to create a data table (with the chart_data passed
to the `charts.html` template) and render a column chart and a pie chart with
that data table. Depending on the device display width the user is using, either
a data table is created with the full data passed to `charts.html`, or a truncated
version is created for smaller mobile devices with only the top 15 tech keywords
to increase readability and create a more positive UX.
- **reset-2025.css**: Contains a set of selectors to reset and standardize typically
used elements used on a web page. From setting default font types and text size,
to removing the default margins on elements and default list styles.
- **styles.css**: Most of the styling is handled though the Bootstrap framework,
but there are a few custom styles that needed to be defined in this file. Things like:
    - Main app title font and colors
    - Search button colors, and states
    - Alert close button for the message banners
    - Page attribution font size
- **layout.html**: The main template that all the other template files are extended off of, containing the structure of things that are the same across all templates such as; the header and navigation, Flask flash messages, the main content container that holds every page's content, and the footer and navigation. This also takes care of linking the Bootstrap framework, app title font, and stylesheets. It lastly contains a small bit of logic to determine what page is active and highlights that navigation menu item for the user.
- **index.html**: Contains the app title, description, and main search form. It also holds the Nominatim user agent for passing along with the API call, logic for changing the state of the search button once clicked and a search is running, and an onclick event that triggers "loading container" text to appear for a better UX.
- **list.html**: A simple page that populates an HTML table with keyword and frequency key/value pairs passed in from either the `"/scrape"` or `"/list"` route. It also uses the users job title and location data as well as the number of job descriptions that were searched to create a dynamic description of the table
- **charts.html**: This file holds links to the Google Charts library and `charts.js`, creates a variable to hold the chart data passed in from the `"/charts"` Flask route, and creates 2 containers to hold the charts rendered by `charts.js`. Just like in `list.html`, it also uses the users job title and location data as well as the number of job descriptions that were searched to create a dynamic description of the charts.
- **about.html**: Provides a bit of background on my path into software development and the choices I made in developing this project
- **no-keywords.html & no-results.html**: Two error pages that handle alerting the user to errors when either no keywords are found for the entered job title, or there are no jobs found for the job title an location entered, respectively. Similar to `list.html` and `charts.html`, they also use templating with the users job title and location data to dynamically provide info about the error.
- **.gitignore**: Contains a list of directories and file types for Git to ignore when syncing with GitHub
- **Dockerfile**: File used to set the parameters for and create a Docker image (used in my Docker-based deployment on [Render](https://render.com/))
- **requirements.txt**: Includes all dependencies needed for the application to run.
- **README.md**: The file that explains all the other files, including itself, which explains all the other files, including itself, which exp---[stack overflow].
### Design Choices:
- Python/Flask
- No database
- Modularized code
    - extract.py
    - keywords.py
    - scrape.py
    - charts.js
    - location.js
    - reset-2025.css
- Typing and custom type class
- Selenium over Beautifulsoup or Scrapy
- Utilizing a `keywords.py` file containing a large set of keywords over a
trained AI or NLP library