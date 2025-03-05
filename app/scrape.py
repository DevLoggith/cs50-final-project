import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# include a limit argument, or just not include logic to continue to next page? 
def scrape_website(title, location, limit):
    driver = set_up_driver()

    try:
        driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4150358483")

        # wait until site has loaded
        # close popup "sign-in" modal
        # place job title and location into respective input fields and search
        # wait for search to complete
        # keep scrolling to bottom of page until no more jobs are loaded ("see more jobs" button appears)
            # alternately waiting each time for new job postings to load
        # scroll back to top of page(?)
        # for each link nested under each <li> job card:
            # follow link nested under each <li> job posting
            # click on <button class="show-more-less-html__button">
            # extract all text nested under <section class="description">
        # return extracted job descriptions

    except Exception as e:
        print(f"An error has occurred: {e}")
    
    finally:
        driver.quit()
    

def set_up_driver():
    chromedriver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") 
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
    return driver


if __name__ == "__main__":
    scrape_website()