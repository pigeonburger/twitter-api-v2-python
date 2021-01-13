# The Twitter API v2 recent search endpoint provides developers with API access to public Tweets posted over the last week. The endpoint, receiving a single search query and responding with matching Tweets.

import requests, configparser, json

# Read the keys from auth.ini and define them
config = configparser.ConfigParser()
config.read('auth.ini')

BEARER_TOKEN = config.get('credentials', 'bearer_token')

headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

query = "from:editvideobot -is:retweet"
tweet_fields = "tweet.fields=author_id"
url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&{tweet_fields}"

response = requests.get(url, headers=headers)

print(response.json())