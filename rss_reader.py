# https://alvinalexander.com/python/python-script-read-rss-feeds-database/
# https://wiki.python.org/moin/RssLibraries

import feedparser
import time
from subprocess import check_output
import sys

def read_remoteok():

    url = 'https://remoteok.io/remote-jobs.rss'

    feed = feedparser.parse(url)
    jobs = []

    for entry in feed.entries:
        job = {}

        if "title" in entry:
            job["title"] = entry.title

        if "company" in entry:
            job["company"] = entry.company
        
        if "link" in entry:
            job["href"] = entry.link

        jobs.append(job)
    
    return jobs

def read_weworkremotely():
    url = 'https://weworkremotely.com/categories/remote-programming-jobs.rss'

    feed = feedparser.parse(url)
    jobs = []

    for entry in feed.entries:
        job = {}

        if "title" in entry:

            char_colon = entry.title.find(':')

            if char_colon != -1:
                job["company"] = entry.title[:char_colon]
                job["title"] = entry.title[(char_colon+2):]
            else:
                job["title"] = entry.title
        
        if "link" in entry:
            job["href"] = entry.link

        jobs.append(job)

    return jobs

read_remoteok()