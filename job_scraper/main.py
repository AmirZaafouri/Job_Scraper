from job_scraper.email.html_generator import generate_html  # Adjust based on your actual function
from job_scraper.spiders.TanitJobs_scraper import search_jobs

if __name__ == "__main__":
    keywords = ['entry-level', 'junior developer', 'software engineer']
    jobs = search_jobs(keywords)
    html_report = generate_html(jobs)  # Ensure that this function is in the correct file
    with open("job_report.html", "w", encoding="utf-8") as file:
        file.write(html_report)

