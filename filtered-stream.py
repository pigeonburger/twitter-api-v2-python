# The filtered stream endpoint group enables developers to filter the real-time stream of public Tweets. This endpoint group's functionality includes multiple endpoints that enable you to create and manage rules, and apply those rules to filter a stream of real-time Tweets that will return matching public Tweets

import requests, configparser, json

# Read the keys from auth.ini and define them
config = configparser.ConfigParser()
config.read('auth.ini')

BEARER_TOKEN = config.get('credentials', 'bearer_token')

headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

response = requests.get("https://api.twitter.com/2/tweets/search/stream/rules", headers=headers)

current_rules = response.json()
print(current_rules)

# Attempts to delete any existing stream rules created prior to running this script
if current_rules is None or "data" not in current_rules:
    pass
else:
    ids = list(map(lambda rule: rule["id"], current_rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post("https://api.twitter.com/2/tweets/search/stream/rules", headers=headers, json=payload)
    print("Deleted existing rules")

# You can add whatever stream rules you want here
sample_rules = [{"value": "dog has:images", "tag": "dog pictures"}, {"value": "cat has:images -grumpy", "tag": "cat pictures"}]
payload = {"add": sample_rules}
response = requests.post("https://api.twitter.com/2/tweets/search/stream/rules", headers=headers, json=payload)

response = requests.get("https://api.twitter.com/2/tweets/search/stream", headers=headers, stream=True)
print(response.status_code)

# Prints the incoming live Tweets as they are tweeted
for response_line in response.iter_lines():
    if response_line:
        json_response = json.loads(response_line)
        print(json_response['data'])