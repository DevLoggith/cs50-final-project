import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import logging
import json
import re


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_browser():
    """Helper function to initialize undetected ChromeDriver"""
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    logger.info("Initializing Chrome browser...")
    return uc.Chrome(options=options)

def search(browser, wait, job_title, location):
    """Helper function to handle search form"""
    logger.info("Waiting for search form...")
    job_input = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    location_input = browser.find_element(By.NAME, "l")
    
    logger.info("Entering search criteria...")
    job_input.send_keys(job_title)
    location_input.send_keys(location)
    location_input.send_keys(Keys.RETURN)

def dismiss_modals(browser):
    """Helper function to dismiss any visible modals"""
    try:
        modals = browser.find_elements(By.CSS_SELECTOR, "[data-js-suggest-better-alert-modal]")
        for modal in modals:
            if modal.is_displayed():
                # first "closes" and then hides the modal
                browser.execute_script("arguments[0].setAttribute('data-closed', 'true');", modal)
                browser.execute_script("arguments[0].style.display = 'none';", modal)
    except Exception as e:
        logger.error(f"Error dismissing modals: {e}")

def dismiss_ads(browser):
    try:
        ad_card = browser.find_element(By.ID, "card")
        if ad_card.is_displayed():
            ad_close_button = browser.find_elements(By.ID, "dismiss-button")
            ad_close_button.click()
    except NoSuchElementException:
        pass
    except Exception as e:
        logger.error(f"Error dismissing ad: {e}")

def navigate_to_next_page(wait, page):
    """Helper function to handle next-page navigation"""
    try:
        next_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "next-page-button"))
        )
        if not next_button:
            logger.info("No more pages available")
            return False, page
        
        next_button.click()
        page += 1
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "show-job-description"))
        )
        return True, page

    except Exception as e:
        logger.error(f"Error navigating to next page: {e}")
        return False, page

def clean_job_descriptions(text):
    """Helper function to clean scraped job descriptions"""
    # convert from WebElement to text and lowercase
    text_lower = text.text.lower()
    # remove all punctuation that would not be used in a tech keyword
    remove_chars = re.sub(r'[,;:()\[\]{}""''\|\?!\\/]', ' ', text_lower)
    # remove extra whitespaces and newlines, rejoin with a single space
    clean_text = " ".join(remove_chars.strip().split())

    return clean_text

def scrape_job_descriptions(job_title, location, limit=10):
    browser = initialize_browser()
    wait = WebDriverWait(browser, 10)
    
    try:
        logger.info("Loading page...")
        browser.get("https://us.jora.com/")
        
        search(browser, wait, job_title, location)
        
        logger.info("Waiting for results...")
        # wait for either the job listings or a "no results" message
        wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, 
                ".show-job-description, .no-results-container"
            ))
        )

        # return empty list if search returns no results
        try:
            browser.find_element(By.CSS_SELECTOR, ".no-results-container")
            logger.info("No search results found")
            return []
        except NoSuchElementException:
           logger.info("Search results found") 
        
        job_descriptions = [{"job_title": job_title, "descriptions": []}]
        descriptions = job_descriptions[0]["descriptions"]
        page = 1

        while len(descriptions) < limit:
            logger.info(f"Scraping page {page}...")

            dismiss_ads(browser)
            dismiss_modals(browser)

            # Find and process job listings
            job_links = wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "show-job-description"))
            )

            for link in job_links:
                if len(descriptions) >= limit:
                    break

                try:
                    current_job = len(descriptions) + 1
                    logger.info(f"Processing job {current_job}...")
                    link.click()
                    wait.until(
                        lambda browser: browser.find_element(
                            By.CSS_SELECTOR,
                            ".jdv-content[data-hidden='false']"
                        )
                    )
                    description = wait.until(
                        EC.presence_of_element_located((By.CLASS_NAME, "job-description-container"))
                    )
                    clean_description = clean_job_descriptions(description)
                    job_descriptions[0]["descriptions"].append({
                            "index": current_job, 
                            "description": clean_description
                        })
                    print(f"Job Description {current_job} scraped successfully")
                    print("-" * 80)
                except Exception as e:
                    logger.error(f"Error processing job {current_job}: {e}")
                    continue
            
            if len(descriptions) < limit:
                should_continue, page = navigate_to_next_page(wait, page)
                if not should_continue:
                    break

        # write output to JSON for testing purposes
        with open("descriptions.json", "w") as file:
            json.dump(job_descriptions, file, indent=4)
        
        return job_descriptions
            
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        logger.info("Closing browser...")
        browser.quit()

job = "software engineer"
location = "cleveland, oh"

scrape_job_descriptions(job, location)
