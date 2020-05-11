# Author: zacfinger.com
# Date: 2020 Q1/Q2
# Title: Jobscraper
####################

import webscraper
import send_email
import json
import credentials
import slackbot

print("Executing ...")

# Declare search parameters
# For example:
# query = 'web+developer'
# location = 'San+Francisco%2C+CA'
query = 'developer'
location = 'Remote'

jobs = []

try:
    # Query jobs from Hacker News API
    # jobs += webscraper.query_HN_jobs()

    # Scrape jobs from first page of Indeed
    jobs += webscraper.scrape_indeed(query, location)

    # Send email report
    # send_email.send_job_report(jobs, query, location)

    # Save local JSON data file
    # https://realpython.com/python-json/#encoding-and-decoding-custom-python-objects
    with open(credentials.json_path + "jobs.json", "w") as write_file:
        json.dump(jobs, write_file)

    # Eventually need to append to JSON file 
    # https://www.google.com/search?client=ubuntu&channel=fs&q=python+append+to+json+file&ie=utf-8&oe=utf-8
    # https://www.geeksforgeeks.org/append-to-json-file-using-python/
    # https://kite.com/python/answers/how-to-append-to-a-json-file-in-python

    count = 0

    message = "Job posts today\n"

    for job in jobs:
        message += "\nCompany: " + job["company"]
        message += "\nRole: " + job["title"]
        message += "\n" + job["href"]
        message += "\n"
        
        if count < 3:
            slackbot.makePost(message)
            count += 1

    print("Success")

except Exception as e:

    print(str(type(e)) + " " + str(e) + " something error happens.")