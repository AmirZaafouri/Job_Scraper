import smtplib
import yaml
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Load email credentials from config.yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

EMAIL_SENDER = config["email"]["sender"]
EMAIL_PASSWORD = config["email"]["password"]
SMTP_SERVER = config["email"]["smtp_server"]
SMTP_PORT = config["email"]["smtp_port"]
EMAIL_RECIPIENT = config["email"]["recipient"]

def format_jobs_html(job_list):
    """Generates an HTML email content for job listings."""
    job_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Job Listings</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 20px; }
            .container { max-width: 600px; margin: auto; padding: 20px; background: #fff; border-radius: 8px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); }
            h2 { text-align: center; color: #333; }
            .job-card { border: 1px solid #ddd; border-radius: 5px; padding: 15px; margin-bottom: 15px; background-color: #fafafa; }
            .job-title { font-size: 18px; font-weight: bold; color: #007BFF; }
            .company { font-size: 16px; color: #555; }
            .details { margin: 10px 0; font-size: 14px; color: #666; }
            .link { display: inline-block; margin-top: 10px; background: #007BFF; color: #fff; padding: 10px; text-decoration: none; border-radius: 5px; }
            .link:hover { background: #0056b3; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Job Listings</h2>
    """

    for job in job_list:
        job_html += f"""
        <div class="job-card">
            <div class="job-title">{job['title']}</div>
            <div class="company">Company: {job['company']}</div>
            <div class="details">Location: {job['location']} | Date Posted: {job['date_posted']} | Experience Required: {job['experience_required']}</div>
            <p>Description: {job['description'][:200]}...</p>
            <a href="{job['link']}" class="link">View Job</a>
        </div>
        """

    job_html += "</div></body></html>"
    return job_html

def send_job_listings(email_recipient, job_list):
    """Sends an email with job listings."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = email_recipient
    msg['Subject'] = "Latest Job Listings"

    email_body = format_jobs_html(job_list)
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