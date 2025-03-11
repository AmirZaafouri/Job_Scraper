import json  # Add this import at the top of your file

def generate_html(jobs, items_per_page=4):
    """Generates a static HTML file to display jobs with pagination."""
    total_jobs = len(jobs)
    num_pages = (total_jobs // items_per_page) + (1 if total_jobs % items_per_page > 0 else 0)

    html_content = """
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
            .pagination { text-align: center; margin-top: 20px; }
            .pagination button { margin: 0 5px; padding: 10px; border: none; background: #007BFF; color: #fff; cursor: pointer; border-radius: 5px; }
            .pagination button:disabled { background: #ccc; cursor: not-allowed; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Job Listings</h2>
            <div id="job-list">
    """

    # Static content generation remains the same
    for i, job in enumerate(jobs):
        html_content += f"""
            <div class="job-card">
                <div class="job-title">{job['title']}</div>
                <div class="company">Company: {job['company']}</div>
                <div class="details">Location: {job['location']} | Date Posted: {job['date_posted']} | Experience Required: {job['experience_required']}</div>
                <p>Description: {job['description'][:150]}...</p>
                <a href="{job['link']}" class="link">View Job</a>
            </div>
        """

    html_content += """
            </div>
            <div class="pagination">
                <button id="prev-btn" onclick="changePage(-1)" disabled>Back</button>
                <button id="next-btn" onclick="changePage(1)">Next</button>
            </div>
        </div>
        <script>
            const jobs = """ + json.dumps(jobs) + """;  // Serialize jobs to JSON
            let currentPage = 1;
            const itemsPerPage = """ + str(items_per_page) + """;
            const totalJobs = """ + str(total_jobs) + """;
            const numPages = """ + str(num_pages) + """; 

            function displayJobs() {
                const jobListDiv = document.getElementById('job-list');
                jobListDiv.innerHTML = ''; // Clear previous jobs

                const start = (currentPage - 1) * itemsPerPage;
                const end = start + itemsPerPage;

                for (let i = start; i < end && i < totalJobs; i++) {
                    const job = jobs[i];  // Now 'jobs' is defined here
                    jobListDiv.innerHTML += `
                        <div class="job-card">
                            <div class="job-title">${job.title}</div>
                            <div class="company">Company: ${job.company}</div>
                            <div class="details">Location: ${job.location} | Date Posted: ${job.date_posted} | Experience Required: ${job.experience_required}</div>
                            <p>Description: ${job.description.substring(0, 150)}...</p>
                            <a href="${job.link}" class="link">View Job</a>
                        </div>
                    `;
                }

                // Update pagination buttons
                document.getElementById('prev-btn').disabled = currentPage === 1;
                document.getElementById('next-btn').disabled = currentPage === numPages;
            }

            function changePage(direction) {
                currentPage += direction;
                displayJobs();
            }

            // Initial display
            displayJobs();
        </script>
    </body>
    </html>
    """
    return html_content  # Add this at the end of your function
