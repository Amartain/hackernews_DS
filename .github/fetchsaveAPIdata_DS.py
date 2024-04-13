import requests
import json
import pandas as pd
from datetime import datetime
import os
import pytz

# Fetch
url = f'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
response = requests.get(url)
top_story_ids = json.loads(response.text)

all_story_details = []

# Fetch details

# VERY IMPORTANT DO NO REMOVE EVEN  IF YOUR SOUL IS IN DANGER!!!!!!111111 (formatted url W/O it the correct data wouldn't be fetched)
story_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'
#i = 0

for story_id in top_story_ids:
    story_response = requests.get(story_url.format(story_id))
    story_details = json.loads(story_response.text)
    all_story_details.append(story_details)
    #i += 1
    #print(i)

df = pd.DataFrame(all_story_details)

df.to_csv('hacker_news_data.csv', index=False)


# Get curr. US Central
central = pytz.timezone('US/Central')
now = datetime.now(central)
file_name = now.strftime("%Y-%m-%d_%H-%M-%S") + ".csv"


file_path = './API_data/'

# Check if the directory exists! --- else it will never work LOL
if not os.path.exists(file_path):
    os.makedirs(file_path)

# need full file path, here combine
full_file_path = os.path.join(file_path, file_name)

# Save it
df.to_csv(full_file_path, index=False)
