# Twitter API V2 Python
These are simpler versions I've based off of the standard Twitter API v2 Python samples that were <a href="https://github.com/twitterdev/Twitter-API-v2-sample-code">provided by Twitter</a> themselves. These ones allow for seamless OAuth1 authentication, without worrying about pasting pins and stuff when it comes to user-based authentication.

These scripts all use <i>user-based authentication</i>, so none of them require Bearer Tokens. Feel free to make a pull request if you adapt any of these scripts for app-based auth (I only needed user auth, so that's why I didn't make them)

<h2>Requirements:</h2>

Python 3 is required.

A Twitter developer account is required. You can <a href="https://developer.twitter.com/en/apply-for-access">apply for one here</a> if you don't already have one.
A Project and an App in the <a href="https://developer.twitter.com/en/portal/dashboard">developer dashboard</a> is also required.

The following things need to be installed:

  - `requests` (install with the command `pip install requests`)
  - `requests_oauthlib` (install with the command `pip install requests-oauthlib`)
  
<h2>Initial setup:</h2>

Clone this repository: `https://github.com/pygeonburger/twitter-api-v2-python`

In order to authenticate to Twitter, you'll need to provide your API key and secret, and your access token and secret. Each Python script here uses `configparser` to fetch these keys from one file, so you don't have to paste them into each individual file.

Open the `auth.ini` file and enter your consumer key, consumer secret, access token and access token secret on their corresponding lines.

Check the name of each file and the comments inside for what each script does. For more info on the Twitter API v2, <a href="https://developer.twitter.com/en/docs/twitter-api">click here to read the docs</a>.

Enjoy playing around with it and feel free to open an issue or message me on Twitter (@pigeonburger) if you have any questions!
