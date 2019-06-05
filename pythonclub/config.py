import os

EMAIL_ADDRESS = "tba@tba.tba"
GITHUB_PROFILE = "tba"
SLACK_CHANNEL = "https://tba.slack.com/messages/tba/"

try:
    EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]
except KeyError:
    pass
try:
    GITHUB_PROFILE = os.environ["GITHUB_PROFILE"]
except KeyError:
    pass
try:
    SLACK_CHANNEL = os.environ["SLACK_CHANNEL"]
except KeyError:
    pass
