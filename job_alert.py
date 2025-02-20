from undetected_chromedriver import Chrome, ChromeOptions
import time
from bs4 import BeautifulSoup

# Function to create a new Chrome instance with cleared cache
def create_chrome_instance():
    options = ChromeOptions()

    # Disable the cache by setting up a fresh session
    options.add_argument("--incognito")  # Use incognito mode to avoid cache
    options.add_argument("--disable-application-cache")  # Disable application cache
    options.add_argument("--disable-cache")  # Disable cache in general
    options.add_argument("--disk-cache-size=0")  # Set cache size to 0 to clear cache
    options.add_argument("--disable-plugins-discovery")  # Disable plugin discovery to reduce potential caching
    options.add_argument("--disable-extensions")  # Disable extensions to avoid any cache from them

    # Create a new instance of Chrome with the specified options
    chrome = Chrome(options=options)
    return chrome

try:
    # Create a new instance of Chrome
    chrome = create_chrome_instance()

    # Navigate to the website
    chrome.get("https://www.tanitjobs.com/jobs/?listing_type%5Bequal%5D=Job&searchId=1733181940.9095&action=search&keywords%5Ball_words%5D=junior+developer&GooglePlace%5Blocation%5D%5Bvalue%5D=&GooglePlace%5Blocation%5D%5Bradius%5D=50")

    # Sleep for a while to let the page load
    time.sleep(60)

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

# Function to filter jobs based on keywords
def filter_jobs(jobs):
    keywords = ['entry-level', 'junior developer', 'software engineer']
    filtered_jobs = [job for job in jobs if any(keyword in job[0].lower() for keyword in keywords)]
    return filtered_jobs

# Function to send email notifications
def send_email(jobs):
    sender = "your-email@gmail.com"
    password = "your-app-password"  # Use an app-specific password here
    receiver = "recipient-email@gmail.com"
    body = "\n".join([f"{title}: {link}" for title, link in jobs])

    msg = MIMEText(body, _charset='utf-8')
    msg["Subject"] = "New Entry-Level Jobs in Tunisia"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)

# Main function to run the scraper
def main():
    #jobs = get_job_listings()
    print(jobs)
    filtered_jobs = filter_jobs(jobs)
    
    if filtered_jobs:
        send_email(filtered_jobs)
    else:
        print("No matching jobs found.")

if __name__ == "__main__":
    main()
