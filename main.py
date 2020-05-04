# Author: zacfinger.com
# Date: 2020 Q1/Q2
# Title: Jobscraper
####################

import webscraper
import send_email

print("Executing ...")

# Declare search parameters
# For example:
# query = 'web+developer'
# location = 'San+Francisco%2C+CA'
query = 'developer'
location = '85719'

jobs = []

try:
    # Query jobs from Hacker News API
    jobs += webscraper.query_HN_jobs()

    # Scrape jobs from first page of Indeed
    jobs += webscraper.scrape_indeed(query, location)

    # Send email report
    send_email.send_job_report(jobs, query, location)

    # eventually need to output to JSON file
    # https://realpython.com/python-json/#encoding-and-decoding-custom-python-objects
    # https://www.google.com/search?client=ubuntu&channel=fs&q=create+json+python3&ie=utf-8&oe=utf-8

    print("Success")

except Exception as e:

    print(str(type(e)) + " " + str(e) + " something error happens.")