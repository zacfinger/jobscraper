# https://github.com/slackapi/python-slackclient
# https://stackoverflow.com/questions/52872580/how-to-respond-with-the-correct-challenge-value-when-trying-to-enable-event-subs
# https://api.slack.com/apps/A013LCCV3QR/event-subscriptions?
# https://api.slack.com/events/url_verification
# http://www.islandtechph.com/2017/10/21/how-to-deploy-a-flask-python-2-7-application-on-a-live-ubuntu-16-04-linux-server-running-apache2/
# http://www.islandtechph.com/2017/10/23/how-to-deploy-a-flask-python-3-5-application-on-a-live-ubuntu-16-04-linux-server-running-apache2/
# https://stackoverflow.com/questions/46463199/no-such-file-or-directory-mod-wsgi-unable-to-connect-to-wsgi-daemon-process
# https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/

# import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi
#from onboarding_tutorial import OnboardingTutorial
import credentials

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(credentials.signing_secret, "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=credentials.slack_bot_token)

#{"channel": {"user_id": OnboardingTutorial}}

#onboarding_tutorials_sent = {}

@slack_events_adapter.on("message")
def message(payload):
    print(payload)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(port=3000)