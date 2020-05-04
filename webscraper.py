import requests
from bs4 import BeautifulSoup

### Scrape Indeed.com ###
### Return Dict object ###
def scrape_indeed(query, location):

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