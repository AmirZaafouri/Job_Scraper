import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

options = uc.options.ChromeOptions()
options.add_argument('--headless')  # Optional: If you need headless mode
options.add_argument('--disable-logging')
options.add_argument('--log-level=3')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

# Clear cache by launching the browser with specific flags
options.add_argument('--incognito')  # Open in incognito mode to avoid cache from previous sessions
options.add_argument('--disk-cache-size=0')  # Disable caching

try:
    # Create a new instance of Chrome with the updated options
    chrome = uc.Chrome(options=options)

    # Navigate to the desired URL
    chrome.get("https://www.tanitjobs.com/jobs/?listing_type%5Bequal%5D=Job&searchId=1733181940.9095&action=search&keywords%5Ball_words%5D=junior+developer&GooglePlace%5Blocation%5D%5Bvalue%5D=&GooglePlace%5Blocation%5D%5Bradius%5D=50")

    # Wait until the page has fully loaded
    WebDriverWait(chrome, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "listing-item"))
    )

    # Get the page source after loading
    page_source = chrome.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find and print job listings
    job_listings = soup.find_all('article', class_='listing-item')
    for job in job_listings:
        title = job.find('div', class_='media-heading').find('a').get_text(strip=True)
        company = job.find('span', class_='listing-item__info--item-company').get_text(strip=True)
        location = job.find('span', class_='listing-item__info--item-location').get_text(strip=True)
        date = job.find('div', class_='listing-item__date').get_text(strip=True)
        description = job.find('div', class_='listing-item__desc').get_text(strip=True)

        print(f"Job Title: {title}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print(f"Date Posted: {date}")
        print(f"Description: {description}")
        print("------")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the browser is closed
    try:
        chrome.quit()
    except Exception as e:
        print(f"Error closing browser: {e}")
