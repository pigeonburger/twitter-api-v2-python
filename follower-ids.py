# THIS SCRIPT ALLOWS YOU TO RETURN THE USER IDS OF THE PEOPLE THAT FOLLOW A SPECIFIED PERSON

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

# Add a Twitter username here
params = {'screen_name': 'editvideobot'}

response = requests.get("https://api.twitter.com/1.1/followers/ids.json", params=params, auth=oauth)

# Print the response
print(response.json())

# Do whatever you want with the result here after.
