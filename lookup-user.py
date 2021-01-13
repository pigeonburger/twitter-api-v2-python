# THIS SCRIPT ALLOWS YOU TO LOOK UP SPECIFIC USERS USING THE TWITTER API V2

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

# User fields are adjustable, options include:
# created_at, description, entities, id, location, name,
# pinned_tweet_id, profile_image_url, protected,
# public_metrics, url, username, verified, and withheld
fields = "created_at,description"
params = {"usernames": "pigeonburger,editvideobot", "user.fields": fields}

response = requests.get("https://api.twitter.com/2/users/by", params=params, auth=oauth)

result = response.json()

# Print the response
print(result)

# Do whatever you want with the result here after.
