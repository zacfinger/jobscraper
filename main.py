# Author: zacfinger.com
# Date: 2020-01-03
# Title: Jobscraper

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Declare search parameters
#query = 'sales'
#location = 'San+Francisco%2C+CA'
query = 'web+developer'
location = '85718'

# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
url = 'https://www.indeed.com/jobs?q='+query+'&l='+location
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup)

