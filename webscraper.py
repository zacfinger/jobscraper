import requests
import json
from bs4 import BeautifulSoup

"""
UpWork search keyword Developer
https://www.upwork.com/ab/feed/jobs/rss?q=developer&sort=recency&user_location_match=1&paging=0%3B10&api_params=1&securityToken=4c27ad8f8b08c2fe44629ae358f3c3597b8daa955903608c556f24229569b9d7270becedd4b40e67ba7885f31cdb4a3329816d7c390b0ef9ac6aad7860c71e8b&userUid=692228455128104960&orgUid=692228455132299265

"""

def categorize_HN_job(job_post):
	"""
	Convert job post JSON from HN into Job dict
	"""
	post_title = job_post["title"]
	index = post_title.lower().find(("is hiring").lower())
	
	#if index != -1:
		#company = title[:index-1]
		#title = 

def query_HN_jobs():
	"""
	API request to HN Jobs
	"""
	job_ids = []
	jobs = []

    # https://www.digitalocean.com/community/tutorials/how-to-use-web-apis-in-python-3
    # https://github.com/HackerNews/API
	api_job_url = 'https://hacker-news.firebaseio.com/v0/jobstories.json'
	headers = {'Content-Type': 'application/json'}
	
	response = requests.get(api_job_url, headers=headers)

	if response.status_code == 200:
		job_ids = json.loads(response.content.decode('utf-8'))
	else:
		print(response.status_code)
	
	for job_id in job_ids:
		job = {}
		
		api_url = 'https://hacker-news.firebaseio.com/v0/item/{0}.json'
		response = requests.get(api_url.format(job_id), headers=headers)
		job_post = json.loads(response.content.decode('utf-8'))

		categorize_HN_job(job_post)
	
		if("title" in job_post and "by" in job_post and "url" in job_post):
			job["title"] = job_post["title"]
			job["company"] = job_post["by"]
			job["href"] = job_post['url']
			jobs.append(job)
	
	return jobs

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
			
			job["company"] = job["company"][1:]

		jobs.append(job)

	return jobs