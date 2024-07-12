import json
from flipkart_client import FlipkartClient

client = FlipkartClient()
tweets = client.get_tweets()

with open('data/flipkart_twitter.json', 'w', encoding='utf-8') as f:
    json.dump(tweets, f, indent=4)

prompt = '''You are an expert in data analytics and a skilled teacher, capable of creating comprehensive documentation from JSON data. Your task is to produce a detailed summary of the provided JSON data. The goal is to prepare the document in a way that ensures anyone reading it can excel in a subsequent multiple-choice quiz based on this data. The summary should cover all key aspects and nuances of the data, ensuring clarity and thorough understanding.

Here is the JSON data for your analysis:

'''

tweets_str = json.dumps(tweets, indent=4)
prompt += f"'''\n{tweets_str}\n'''"

with open('data/prompt.txt', 'w', encoding='utf-8') as f:
    f.write(prompt)