# Job Scraper TN

A personal job scraping tool created to automatically find job opportunities on **TanitJobs** and filter them according to my job-search criteria.

The goal is to avoid manually checking job offers and receive only relevant opportunities.

---

## 🎯 Goal

The project currently:

1. Searches TanitJobs using predefined keywords.
2. Extracts job offers.
3. Removes duplicate offers.
4. Checks the required experience.
5. Filters irrelevant offers.
6. Generates an HTML report.
7. Sends the results by email.

---

## 🏗️ Project Structure

```text
Job_Scraper/
│
├── job_scraper/
│   ├── main.py                    # Application entry point
│   │
│   ├── spiders/
│   │   └── TanitJobs_scraper.py   # TanitJobs scraping + filtering
│   │
│   ├── email/
│   │   ├── email_sender.py        # Send email
│   │   └── html_generator.py      # Generate HTML report
│   │
│   └── utils/
│       ├── config.yaml            # Configuration
│       └── logger.py              # Logging (TODO)
│
├── requirements.txt
├── README.md
│
├── job_alert.py                   # Old prototype
├── Test.py                        # Old prototype/test
└── By_Pass_Captcha.py             # Old captcha experiment
```

---

## 🔄 Current Flow

```text
main.py
   ↓
TanitJobs scraper
   ↓
Search using keywords
   ↓
Extract job information
   ↓
Remove duplicate URLs
   ↓
Open job details
   ↓
Extract experience requirement
   ↓
Filter jobs
   ↓
Generate HTML report
   ↓
Send email
```

---

## 🔍 Current Filters

### Keywords

Currently defined in `main.py`:

```python
[
    "entry-level",
    "junior developer",
    "software engineer"
]
```

### Experience

Current rule:

```text
Keep job if:
    experience < 2 years
    OR
    experience is not specified
```

Other filters are **not implemented yet**.

Potential future filters:

* Technologies / skills
* Location
* Contract type
* Remote / onsite
* Date posted
* Job title
* Company
* Salary

---

## 🛠️ Technologies

* Python 3.11
* DrissionPage
* BeautifulSoup4
* PyYAML
* smtplib
* requests

DrissionPage is used to interact with TanitJobs through a real Chromium browser.

---

## ▶️ How to Run

From the project root:

```bash
cd Job_Scraper
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Run:

```bash
python -m job_scraper.main
```

> Do not run `python job_scraper/main.py` directly because the project uses package imports.

---

## ⚙️ Configuration

Email configuration is stored in:

```text
job_scraper/utils/config.yaml
```

Expected configuration:

```yaml
email:
  sender: "your@email.com"
  password: "your-app-password"
  smtp_server: "smtp.gmail.com"
  smtp_port: 587
  recipient: "recipient@email.com"
```

⚠️ **Never commit real email credentials to Git.**

Prefer environment variables or another secure configuration method in the future.

---

## ⚠️ Known Issues / Things to Check

Before working on new features:

* [ ] `config.yaml` is currently empty
* [ ] `requirements.txt` needs to include all required packages
* [ ] Scraper depends heavily on TanitJobs HTML structure
* [ ] Experience is checked by opening each job individually → can be slow
* [ ] Errors during scraping are not handled very well
* [ ] Keywords are hard-coded
* [ ] Experience limit is hard-coded
* [ ] Only the first search-results page is currently scraped
* [ ] No persistent database/storage
* [ ] No scheduling/automatic execution
* [ ] Logging is not implemented

---

## 🚧 Current State

### Working

* [x] TanitJobs scraping
* [x] Multiple keyword searches
* [x] Job extraction
* [x] Duplicate removal
* [x] Experience extraction
* [x] Experience filtering
* [x] HTML report
* [x] Email report

### Not implemented yet

* [ ] Technology/skill filtering
* [ ] Advanced filtering system
* [ ] New-job-only notifications
* [ ] Automatic scheduling
* [ ] Other Tunisian job websites

---

## 🧭 Next Development Direction

The main objective is to evolve the project from a simple scraper into a **personal job-search assistant**.

Possible future flow:

```text
Scraping
   ↓
Normalize Job Data
   ↓
Filtering
   ├── Title
   ├── Experience
   ├── Technologies
   ├── Location
   ├── Contract
   └── Remote
   ↓
Ranking / Matching
   ↓
Relevant Jobs
   ↓
HTML + Email
```

Keep the project simple and pragmatic.

**Do not introduce unnecessary frameworks or architecture unless they solve an actual problem.**

---

## 📝 When Coming Back to This Project

If I haven't worked on this project for a long time:

1. Read this README.
2. Check the current Git status.
3. Read `job_scraper/main.py`.
4. Read `job_scraper/spiders/......_scraper.py`.
5. Check `requirements.txt`.
6. Check whether the site website structure has changed.
7. Run the project before making major changes.
8. Check the TODO / issues before implementing new features.

### Important

**Do not immediately rewrite the project.**

First understand what is currently working, then improve it incrementally.
