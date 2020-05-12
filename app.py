# https://github.com/slackapi/python-slackclient

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
slack_web_client = credentials.slack_bot_token

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