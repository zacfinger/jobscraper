# Author: zacfinger.com
# Date: 2020 Q1/Q2
# Title: Jobscraper
####################

import webscraper
import send_email

# Declare search parameters
# For example:
# query = 'web+developer'
# location = 'San+Francisco%2C+CA'
query = 'QA analyst'
location = '85719'

jobs = []

jobs += webscraper.scrape_indeed(query, location)
send_email.send_job_report(jobs, query, location)

print("\nSuccess")