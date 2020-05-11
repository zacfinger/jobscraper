# https://github.com/slackapi/python-slackclient/wiki/Migrating-to-2.x
# https://stackoverflow.com/questions/44048855/slack-bot-scope-missing-while-making-api-request

from slack import WebClient
import credentials

def makeTextPost(message):
    client = WebClient(credentials.slack_bot_token, timeout=30)
    client.api_call('chat.postMessage', json={
        'channel': 'general',
        'text': message})

    # Note: That while the above is allowed, the more efficient way to call that API is like this:
    # client.chat_postMessage(
    #   channel='C0123456',
    #   text='Hi!')

def postJob(job):
    client = WebClient(credentials.slack_bot_token, timeout=30)
    client.api_call('chat.postMessage', json={
        'channel': 'general',
        'blocks': [
                {
                    "type": "section",
                    "text": {
        "type": "mrkdwn",
        "text": ":star: " + job["company"] + " <" + job["href"] + "|" + job["title"] + ">:star:"
                            }
                }
        ]
    })