# The Twitter API v2 recent search endpoint provides developers with API access to public Tweets posted over the last week. The endpoint, receiving a single search query and responding with matching Tweets.

import requests, configparser, json

# Read the keys from auth.ini and define them
config = configparser.ConfigParser()
config.read('auth.ini')

BEARER_TOKEN = config.get('credentials', 'bearer_token')

headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

params = {
    'query': 'from:editvideobot -is:retweet',
    'tweet.fields': 'author_id'
}

url = "https://api.twitter.com/2/tweets/search/recent"

response = requests.get(url, headers=headers, params=params)

print(response.json())