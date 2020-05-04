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
query = 'QA engineer'
location = '85719'

jobs = []

# jobs += webscraper.query_HN_jobs()
webscraper.query_HN_jobs()

#jobs += webscraper.scrape_indeed(query, location)
#send_email.send_job_report(jobs, query, location)

# eventually need to output to JSON file
# https://realpython.com/python-json/#encoding-and-decoding-custom-python-objects
# https://www.google.com/search?client=ubuntu&channel=fs&q=create+json+python3&ie=utf-8&oe=utf-8

print("\nSuccess")