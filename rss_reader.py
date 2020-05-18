# https://alvinalexander.com/python/python-script-read-rss-feeds-database/
# https://wiki.python.org/moin/RssLibraries

import feedparser
import time
from subprocess import check_output
import sys

def read_remoteok():

    url = 'https://remoteok.io/remote-jobs.rss'
    #url = 'https://weworkremotely.com/categories/remote-programming-jobs.rss'

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