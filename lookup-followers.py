# THIS SCRIPT ALLOWS YOU TO LOOK UP THE FOLLOWERS OF A SPECIFIC USER USING THE TWITTER API V2

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

params = {"user.fields": "created_at"}

user_id = 1299121724684869633
url = f"https://api.twitter.com/2/users/{user_id}/followers"

response = requests.get(url, params=params, auth=oauth)

result = response.json()

# Print the response
print(result)

# Do whatever you want with the result here after.
