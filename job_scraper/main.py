from job_scraper.email.email_sender import send_job_listings
from job_scraper.email.html_generator import generate_html  # Adjust based on your actual function
from job_scraper.spiders.TanitJobs_scraper import search_jobs

if __name__ == "__main__":
    keywords = ['entry-level', 'junior developer', 'software engineer']
    jobs = search_jobs(keywords)
    print(jobs)
    with open("job_report.html", "w", encoding="utf-8") as file:
        file.write(html_report)
    recipient_email = "amirzaafouri1@gmail.com"  
    send_job_listings(recipient_email, html_report)
