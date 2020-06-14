# Author: zacfinger.com
# Date: 2020 Q1/Q2
# Title: Jobscraper
####################

import webscraper
import send_email
import json
import jobscraper_credentials
import slackbot
import rss_reader
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate(jobscraper_credentials.serviceAccount_json)
firebase_admin.initialize_app(cred, {
  'projectId': jobscraper_credentials.project_id,
})

db = firestore.client()

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
    jobs += webscraper.query_HN_jobs()

    # Scrape jobs from first page of Indeed
    jobs += webscraper.scrape_indeed(query, location)

    # Read jobs from remoteok.io RSS feed
    jobs += rss_reader.read_remoteok()

    # Read jobs from weworkremotely.com
    jobs += rss_reader.read_weworkremotely()
    
    # Send email report
    # send_email.send_job_report(jobs, query, location)

    # Save local JSON data file
    # https://realpython.com/python-json/#encoding-and-decoding-custom-python-objects
    with open(jobscraper_credentials.json_path + "jobs.json", "w") as write_file:
        json.dump(jobs, write_file)

    # Eventually need to append to JSON file 
    # https://www.google.com/search?client=ubuntu&channel=fs&q=python+append+to+json+file&ie=utf-8&oe=utf-8
    # https://www.geeksforgeeks.org/append-to-json-file-using-python/
    # https://kite.com/python/answers/how-to-append-to-a-json-file-in-python

    count = 0

    for job in jobs:
        if count < 3:
            #slackbot.postJob(job)
            count += 1
    
    doc_ref = db.collection(u'jobs').document(u'test_data')
    doc_ref.set({
        u'company': u'Test Company 2020-06-13',
        u'title': u'Test Title 2020-06-13',
        u'href': 'https://google.com'
    })

    print("Success")

except Exception as e:

    print(str(type(e)) + " " + str(e) + " something error happens.")