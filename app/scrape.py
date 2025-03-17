import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_job_descriptions(job_title, location, limit=45):
    # Initialize undetected ChromeDriver
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    logger.info("Initializing Chrome browser...")
    browser = uc.Chrome(options=options)
    wait = WebDriverWait(browser, 10)
    
    try:
        logger.info("Loading page...")
        browser.get("https://us.jora.com/")
        
        logger.info("Waiting for search form...")
        job_input = wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        location_input = browser.find_element(By.NAME, "l")
        
        logger.info("Entering search criteria...")
        job_input.send_keys(job_title)
        location_input.send_keys(location)
        location_input.send_keys(Keys.RETURN)
        
        logger.info("Waiting for results...")
        # wait for either the job listings or a "no results" message
        # TODO: handle case where no results are returned
        wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, 
                ".show-job-description, .no-results-container"
            ))
        )
        
        # set limit or scrape all job postings available per search?
        job_descriptions = []
        page = 1

        def dismiss_modals(browser):
            # """Helper function to dismiss any visible modals"""
            try:
                modals = browser.find_elements(By.CSS_SELECTOR, "[data-js-suggest-better-alert-modal]")
                for modal in modals:
                    if modal.is_displayed():
                        browser.execute_script("arguments[0].setAttribute('data-closed', 'true');", modal)
            except Exception as e:
                logger.error(f"Error dismissing modals: {e}")

        while len(job_descriptions) < limit:
            logger.info(f"Scraping page {page}...")

            dismiss_modals(browser)

            # Find and process job listings
            job_links = wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "show-job-description"))
            )

            for link in job_links:
                if len(job_descriptions) >= limit:
                    break

                try:
                    current_job = len(job_descriptions) + 1
                    logger.info(f"Processing job {current_job}...")
                    link.click()
                    description = wait.until(
                        EC.presence_of_element_located((By.CLASS_NAME, "job-description-container"))
                    )
                    clean_description = " ".join(description.text.strip().split())
                    job_descriptions.append({
                        "index": current_job,
                        "description": clean_description
                    })
                    print(f"Job Description {current_job} scraped successfully")
                    print("-" * 80)
                except Exception as e:
                    logger.error(f"Error processing job {current_job}: {e}")
                    continue
            
            if len(job_descriptions) < limit:
                try:
                    next_button = wait.until(
                        EC.presence_of_element_located((By.CLASS_NAME, "next-page-button"))
                    )
                    if not next_button:
                        logger.info("No more pages available")
                        break
                    else:
                        next_button.click()
                        page += 1
                        wait.until(
                            EC.presence_of_element_located((By.CLASS_NAME, "show-job-description"))
                        )

                except Exception as e:
                    logger.error(f"Error navigating to next page: {e}")
                    break

        return job_descriptions
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        logger.info("Closing browser...")
        browser.quit()

job = "software developer"
location = "san francisco, ca"
scrape_job_descriptions(job, location)
