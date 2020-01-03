# Author: zacfinger.com
# Date: 2020-01-03
# Title: Jobscraper

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import credentials

# Declare search parameters
#query = 'sales'
#location = 'San+Francisco%2C+CA'
query = 'web+developer'
location = '85718'

# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
url = 'https://www.indeed.com/jobs?q='+query+'&l='+location
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all class matching 'jobsearch-SerpJobCard unifiedRow row result clickcard'
mydivs = soup.findAll("a", {"class": "jobtitle turnstileLink"})

#print(soup)

for div in mydivs:
	print(div['title'])

def send_email():
	# https://stackoverflow.com/questions/17759860/python-2-smtpserverdisconnected-connection-unexpectedly-closed/33121151
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Daily Job Report: " + query + ", " + location
	msg['From'] = credentials.recipient
	msg['To'] = credentials.sender

	# Create the body of the message (a plain-text and an HTML version).
	html = soup

	# Record the MIME types of both parts - text/plain and text/html.
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part2)

	# Send the message via local SMTP server.
	s = smtplib.SMTP_SSL('smtp.gmail.com')
	# https://stackoverflow.com/questions/55800902/smtplib-smtpnotsupportederror-smtp-auth-extension-not-supported-by-server
	# https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
	s.ehlo()

	# do the smtp auth; sends ehlo if it hasn't been sent already
	s.login(credentials.sender, credentials.password)

	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	s.sendmail(credentials.sender, credentials.recipient, msg.as_string())
	s.quit()

print("\nSuccess")