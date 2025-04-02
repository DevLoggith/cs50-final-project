import re
from keywords import keywords_set
# from scrape import job_descriptions

# TODO: figure out how to loop through each description in job_descriptions, extract
# the keywords based on imported keywords_set, and add them to a dict with
# key/value pairs like so: {"Java": 6, "c#"; 4} to be returned and passed to app.py

# needs function that loops through job_descriptions, extracts keywords per description,
# and either adds them to a dictionary starting with a value of one, or increasing
# the found keyword's value by 1. then returns said dictionary to be passed to
# app.py for creating lists and charts/graphs


keywords = keywords_set
description = "i like c# and java and c# and javascript and c# too"

def find_keywords(keywords, description):
# helper function?
    keywords_present = set()

    for keyword in keywords:
        # escapes special characters in keywords like 'c#' & '.net"
        escaped_keyword = re.escape(keyword)
        # targets any whitespace or specified punctuation at word boundaries
        pattern = fr'(?:^|[\s.]){escaped_keyword}(?:$|[\s.])'

        if re.search(pattern, description):
            keywords_present.add(keyword)

    return keywords_present
