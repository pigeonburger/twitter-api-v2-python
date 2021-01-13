# The sampled stream endpoint delivers a roughly 1% random sample of publicly available Tweets in real-time. With it, you can identify and track trends, monitor general sentiment, monitor global events, and much more.

import requests, configparser, json

# Read the keys from auth.ini and define them
config = configparser.ConfigParser()
config.read('auth.ini')

BEARER_TOKEN = config.get('credentials', 'bearer_token')

headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

response = requests.get("https://api.twitter.com/2/tweets/sample/stream", headers=headers, stream=True)
print(response.status_code)

for response_line in response.iter_lines():
    if response_line:
        json_response = json.loads(response_line)
        print(json_response['data'])