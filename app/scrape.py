import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_job_descriptions(job_title, location, limit=3):
    # Initialize undetected ChromeDriver
    options = uc.ChromeOptions()
    options.headless = True  # Run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    logger.info("Initializing Chrome browser...")
    browser = uc.Chrome(options=options)
    wait = WebDriverWait(browser, 20)
    
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
        time.sleep(5)
        
        # Find and process job listings
        job_links = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "show-job-description"))
        )
        
        job_descriptions = []
        for i, link in enumerate(job_links[:limit], 1):
            try:
                logger.info(f"Processing job {i}...")
                link.click()
                time.sleep(2)
                description = wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, "job-description-container"))
                )
                clean_description = " ".join(description.text.strip().split())
                job_descriptions.append({
                    "index": i,
                    "description": clean_description
                })
                print(f"Job Description {i} scraped successfully")
                print("-" * 80)
            except Exception as e:
                logger.error(f"Error processing job {i}: {str(e)}")
                continue

        print(job_descriptions)
        return job_descriptions
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        logger.info("Closing browser...")
        browser.quit()

job = "software programmer"
location = "cleveland, oh"
scrape_job_descriptions(job, location)
