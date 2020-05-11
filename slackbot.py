# https://github.com/slackapi/python-slackclient/wiki/Migrating-to-2.x

from slack import WebClient
import credentials

def makePost(message):
    client = WebClient(credentials.slack_bot_token, timeout=30)
    client.api_call('chat.postMessage', json={
        'channel': 'general',
        'text': message})

    # Note: That while the above is allowed, the more efficient way to call that API is like this:
    # client.chat_postMessage(
    #   channel='C0123456',
    #   text='Hi!')