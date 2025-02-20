from undetected_chromedriver import Chrome
import time
from bs4 import BeautifulSoup

# create a new instance of Chrome
chrome = Chrome()

# navigate to the website
chrome.get("https://www.tanitjobs.com/jobs/?listing_type%5Bequal%5D=Job&searchId=1733181940.9095&action=search&keywords%5Ball_words%5D=junior+developer&GooglePlace%5Blocation%5D%5Bvalue%5D=&GooglePlace%5Blocation%5D%5Bradius%5D=50")

# sleep for a while to let the page load
time.sleep(60)

# get the page source after loading
page_source = chrome.page_source

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find all job listings
job_listings = soup.find_all('article', class_='listing-item')

# Loop through each job listing and extract details
for job in job_listings:
    title = job.find('div', class_='media-heading').find('a').get_text(strip=True)
    company = job.find('span', class_='listing-item__info--item-company').get_text(strip=True)
    location = job.find('span', class_='listing-item__info--item-location').get_text(strip=True)
    date = job.find('div', class_='listing-item__date').get_text(strip=True)
    description = job.find('div', class_='listing-item__desc').get_text(strip=True)

    # Print the job details
    print(f"Job Title: {title}")
    print(f"Company: {company}")
    print(f"Location: {location}")
    print(f"Date Posted: {date}")
    print(f"Description: {description}")
    print("------")

# close the browser
chrome.close()
