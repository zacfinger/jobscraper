import credentials
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create HTML body of email
# Send email
def send_job_report(jobs, query, location):

	# Construct email body in HTML
	html = ""

	for job in jobs:
		html += "<p>"
		html += "<strong><a href=\""
		html += job["href"] + "\">"
		html += job["title"] + "</a></strong>"
		if(job["company"]):
			html += "<ul><li><small>" + job["company"] + "</small></li></ul>"
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