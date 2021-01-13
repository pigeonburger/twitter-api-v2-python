# THIS SCRIPT ALLOWS YOU TO LOOK UP SPECIFIC TWEETS USING THE TWITTER API V2

# Import required libraries
import requests, configparser
from requests_oauthlib import OAuth1

# Read the keys from auth.ini and define them
config = configparser.ConfigParser()
config.read('auth.ini')

CONSUMER_KEY = config.get('credentials', 'consumer_key')
CONSUMER_SECRET = config.get('credentials', 'consumer_secret')
ACCESS_TOKEN = config.get('credentials', 'access_token')
ACCESS_TOKEN_SECRET = config.get('credentials', 'access_token_secret')

oauth = OAuth1(CONSUMER_KEY,
  client_secret=CONSUMER_SECRET,
  resource_owner_key=ACCESS_TOKEN,
  resource_owner_secret=ACCESS_TOKEN_SECRET)

# Include the ID(s) of the tweets you want to look up, and you can also choose what fields you want to return in the response.
params = {"ids": "1278747501642657792", "tweet.fields": "created_at"}

# Making the request
response = requests.get("https://api.twitter.com/2/tweets", params=params, auth=oauth)

result = response.json()

# Print the response
print(result)

# Do whatever you want with the result here after.
