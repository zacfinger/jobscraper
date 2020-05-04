# Author: zacfinger.com
# Date: 2020 Q1/Q2
# Title: Jobscraper
####################

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import credentials

### Scrape Indeed.com ###
### Return Dict object ###
def scrape_indeed():

	jobs = []

	# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
	url = 'https://www.indeed.com/jobs?q='+query+'&l='+location
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")

	# Find all class matching job results
	mydivs = soup.findAll("div", {"class": "jobsearch-SerpJobCard unifiedRow row result"})

	for div in mydivs:
		
		job = {}

		# https://stackoverflow.com/questions/6287529/how-to-find-children-of-nodes-using-beautifulsoup
		links = div.findChildren("a", {"class": "jobtitle turnstileLink"})
		
		for link in links:
			# https://stackoverflow.com/questions/2612548/extracting-an-attribute-value-with-beautifulsoup
			job["title"] = link["title"]
			job["href"] = "https://indeed.com" + link["href"]

		spans = div.findChildren("span", {"class": "company"})

		for span in spans:
			# https://stackoverflow.com/questions/22003302/beautiful-soup-just-get-the-value-inside-the-tag
			#companies = span.findChildren("a", {"class": "turnstileLink"})
			companies = span.findChildren()
			if(len(companies) >= 1):
				job["company"] = companies[0].string
			else:
				job["company"] = span.string

		jobs.append(job)

	return jobs

# Create HTML body of email
# Send email
def send_email():

	# Construct email body in HTML
	html = ""

	for job in jobs:
		html += "<p>"
		html += "<strong><a href=\""
		html += job["href"] + "\">"
		html += job["title"] + "</a></strong>"
		if(job["company"]):
			html += "<ul><li><small>" + job["company"] + "</small></li></ul>"
		else:
			print(job["title"])
		html += "</p><hr />"

	# https://stackoverflow.com/questions/17759860/python-2-smtpserverdisconnected-connection-unexpectedly-closed/33121151
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Daily Job Report: " + query + ", " + location
	msg['From'] = credentials.recipient
	msg['To'] = credentials.sender

	# Create the body of the message (a plain-text and an HTML version).
	#html = soup

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

# Declare search parameters
query = 'developer'
#location = 'San+Francisco%2C+CA'
#query = 'web+developer'
location = '85719'

jobs = scrape_indeed()
send_email()

print("\nSuccess")