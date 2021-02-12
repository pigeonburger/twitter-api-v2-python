# THIS SCRIPT ALLOWS YOU TO RETURN THE USER OBJECTS OF THE USERS A SPECIFIED ACCOUNT FOLLOWS

# Import required libraries
import requests, configparser
from requests_oauthlib import OAuth1

# Read the keys from auth.ini and define them
config = configparser.ConfigParser()
config.read('backupauth.ini')

CONSUMER_KEY = config.get('credentials', 'consumer_key')
CONSUMER_SECRET = config.get('credentials', 'consumer_secret')
ACCESS_TOKEN = config.get('credentials', 'access_token')
ACCESS_TOKEN_SECRET = config.get('credentials', 'access_token_secret')

oauth = OAuth1(CONSUMER_KEY,
  client_secret=CONSUMER_SECRET,
  resource_owner_key=ACCESS_TOKEN,
  resource_owner_secret=ACCESS_TOKEN_SECRET)


id = 1299121724684869633

response = requests.get(f"https://api.twitter.com/2/users/{id}/following", auth=oauth)

# Print the response
print(response.json())

# Do whatever you want with the result here after.