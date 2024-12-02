import requests
from lxml import html
import json

def scrape_jobs(keyword):
    """Scrape job listings for a specific role from Wellfound using XPath."""
    url = f"https://wellfound.com/role/{keyword}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch data. Please try again later."}

    tree = html.fromstring(response.content)
    jobs = []

    # Locate all job cards using XPath (outside the loop)
    job_cards = tree.xpath('//*[@id="main"]/div[4]/div[2]/div/div/div')

    for job_card in job_cards:
        try:
            # Extract company name
            company_name = job_card.xpath('.//h2[@class="inline text-md font-semibold"]/text()')
            company_name = company_name[0].strip() if company_name else "N/A"
        except Exception as e:
            print(f"Error extracting company name: {e}")
            company_name = "N/A"

        try:
            # Extract company slogan
            company_slogan = job_card.xpath('.//span[@class="text-xs text-neutral-1000"]/text()')
            company_slogan = company_slogan[0].strip() if company_slogan else "N/A"
        except Exception as e:
            print(f"Error extracting company slogan: {e}")
            company_slogan = "N/A"

        try:
            # Extract company page URL
            company_url = job_card.xpath('.//a[contains(@href, "/company")]/@href')
            company_url = f"https://wellfound.com{company_url[0]}" if company_url else "N/A"
        except Exception as e:
            print(f"Error extracting company URL: {e}")
            company_url = "N/A"

        # Extract job listings (job openings) for the current company
        Job_openings = []

        try:
            job_listings = job_card.xpath('.//div[@class="mb-4 w-full px-4"]')  # Fix job listings XPath
            for job in job_listings:
                try:
                    # Extract job title
                    job_title = job.xpath('.//a[contains(@href, "/jobs")]/text()')
                    job_title = job_title[0].strip() if job_title else "N/A"

                    # Extract job listing URL
                    job_url = job.xpath('.//a[contains(@href, "/jobs")]/@href')
                    job_url = f"https://wellfound.com{job_url[0]}" if job_url else "N/A"
                except Exception as e:
                    print(f"Error extracting job title or URL: {e}")
                    job_title, job_url = "N/A", "N/A"
                
                # Append job details to the Job_openings list
                Job_openings.append({
                    "job_title": job_title,
                    "job_url": job_url
                })
        except Exception as e:
            print(f"Error extracting job openings: {e}")
            Job_openings = []

        # Append job details (company + job openings) to the jobs list
        jobs.append({
            "company_name": company_name,
            "company_slogan": company_slogan,
            "company_url": company_url,
            "Job_openings": Job_openings,
        })

    return jobs
