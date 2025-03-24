import os
import smtplib
import yaml
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from job_scraper.email.html_generator import generate_html

# Get the absolute path to the 'config.yaml' file
config_path = os.path.join(os.path.dirname(__file__), '..', 'utils', 'config.yaml')

# Load config.yaml
with open(config_path, "r") as file:
    config = yaml.safe_load(file)

EMAIL_SENDER = config["email"]["sender"]
EMAIL_PASSWORD = config["email"]["password"]
SMTP_SERVER = config["email"]["smtp_server"]
SMTP_PORT = config["email"]["smtp_port"]
EMAIL_RECIPIENT = config["email"]["recipient"]

def send_job_listings(email_recipient, html_report):
    """Sends an email with job listings."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = email_recipient
    msg['Subject'] = "Latest Job Listings"

    email_body = html_report
    msg.attach(MIMEText(email_body, "html"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, email_recipient, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")