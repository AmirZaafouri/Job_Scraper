import os
import smtplib
import yaml
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_job_listings(email_recipient, html_report):
    """Sends an email with job listings."""

    # Load config inside the function so a missing/empty config.yaml
    # does not crash the entire application on import.
    config_path = os.path.join(os.path.dirname(__file__), '..', 'utils', 'config.yaml')
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    email_sender = config["email"]["sender"]
    email_password = config["email"]["password"]
    smtp_server = config["email"]["smtp_server"]
    smtp_port = config["email"]["smtp_port"]

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = "Latest Job Listings"

    msg.attach(MIMEText(html_report, "html"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_recipient, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
