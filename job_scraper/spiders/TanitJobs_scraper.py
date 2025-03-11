from DrissionPage import ChromiumPage
from bs4 import BeautifulSoup
import re

def get_experience_requirement(job_link, page):
    """
    Extracts the experience requirement from a job posting.
    :param job_link: URL of the job posting.
    :param page: ChromiumPage instance to navigate the job details page.
    :return: Minimum years of experience required, or None if not found.
    """
    try:
        page.get(job_link)
        page.wait.ele_displayed("div.infos_job_details", timeout=5)
        soup = BeautifulSoup(page.html, 'html.parser')
        
        # Find the 'Experience' section
        exp_section = soup.find("dt", string="Experience :")
        if exp_section:
            exp_text = exp_section.find_next_sibling("dd").get_text(strip=True)
            match = re.search(r"(\d+)", exp_text)  # Extract the first number (years of experience)
            if match:
                return int(match.group(1))  # Convert to integer

    except Exception as e:
        print(f"Error fetching experience for {job_link}: {e}")
    
    return None  # Return None if experience data is missing


def search_jobs(keywords):
    """
    Searches for jobs on TanitJobs based on multiple keywords, avoiding duplicates, and filtering by experience.
    :param keywords: A list of job titles or keywords to search for.
    :return: List of unique job dictionaries matching experience criteria.
    """
    p = ChromiumPage()
    all_jobs = []
    seen_links = set()

    try:
        for keyword in keywords:
            search_url = f"https://www.tanitjobs.com/jobs/?action=search&keywords%5Ball_words%5D={keyword.replace(' ', '+')}"
            p.get(search_url)
            p.wait.ele_displayed("article.listing-item", timeout=10)

            soup = BeautifulSoup(p.html, 'html.parser')
            jobs = soup.find_all('article', class_='listing-item')

            for job in jobs:
                try:
                    title_elem = job.find('div', class_='media-heading').find('a')
                    company_elem = job.find('span', class_='listing-item__info--item-company')
                    location_elem = job.find('span', class_='listing-item__info--item-location')
                    date_elem = job.find('div', class_='listing-item__date')
                    description_elem = job.find('div', class_='listing-item__desc')

                    title = title_elem.get_text(strip=True) if title_elem else "N/A"
                    company = company_elem.get_text(strip=True) if company_elem else "N/A"
                    location = location_elem.get_text(strip=True) if location_elem else "N/A"
                    date = date_elem.get_text(strip=True) if date_elem else "N/A"
                    description = description_elem.get_text(strip=True) if description_elem else "N/A"
                    
                    # Fix job link extraction
                    raw_link = title_elem["href"] if title_elem else ""
                    if raw_link.startswith("/job/"):  
                        job_link = f"https://www.tanitjobs.com{raw_link}"  
                    else:
                        job_link = raw_link  

                    if job_link and job_link not in seen_links:
                        experience = get_experience_requirement(job_link, p)
                        if experience is None or experience < 2:  # Accept only jobs requiring <2 years
                            seen_links.add(job_link)
                            all_jobs.append({
                                "keyword": keyword,
                                "title": title,
                                "company": company,
                                "location": location,
                                "date_posted": date,
                                "description": description,
                                "link": job_link,
                                "experience_required": experience if experience is not None else "Not specified"
                            })
                
                except AttributeError:
                    continue  

        return all_jobs

    finally:
        p.quit()

# Example Usage
if __name__ == "__main__":
    keywords = ['entry-level', 'junior developer', 'software engineer']
    jobs = search_jobs(keywords)

    print(f"Total unique jobs found: {len(jobs)}\n")

    for job in jobs:
        print(f"Keyword: {job['keyword']}")
        print(f"Job Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print(f"Date Posted: {job['date_posted']}")
        print(f"Experience Required: {job['experience_required']}")
        print(f"Description: {job['description'][:150]}...")
        print(f"Job Link: {job['link']}")
        print("------")
