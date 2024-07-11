import json
from flipkart_client import FlipkartClient

client = FlipkartClient()
tweets = client.get_tweets()

with open('flipkart_twitter.json', 'w', encoding='utf-8') as f:
    json.dump(tweets, f, indent=4)