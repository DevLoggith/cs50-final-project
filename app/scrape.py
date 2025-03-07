import mechanicalsoup
import time


q = "software engineer"
l = "cleveland, oh"

browser = mechanicalsoup.StatefulBrowser()
browser.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
browser.open(f"https://us.jora.com/j?sp=homepage&trigger_source=homepage&q={q}&l={l}")

print(browser.page)


# include a limit argument, or just not include logic to continue to next page? 
# def scrape_website(title, location, limit):

    # wait until site has loaded
    # place job title and location into respective input fields
    # search
    # wait for search to complete
    # for each page
        # for each <li>
            # click each <li> under the <ul id="job-list"> to open the <aside>
            # wait to load
            # scrape all text nested under <div data-testid="viewJobBodyJobFullDescriptionContent"> (or <div class="css-cxpe4v") 20 per page
                # format scraped job description
                # remove new lines, empty lines, and punctuation
                # extract keywords via SpaCy and pre-defined tech_keywords object therein
            # follow next page link (<a class="css-1puj5o8" href="">)
    # return __ of keywords


# Scraping seems to be more of a dead end. most sites block with anti-bot measures
# or captchas. look into accessing an API like jobdataapi?