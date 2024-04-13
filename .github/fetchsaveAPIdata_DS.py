import requests
import json
import pandas as pd
from datetime import datetime
import os
import pytz

# Fetch data
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
data = response.json()

# Convert to pandas
df = pd.DataFrame(data)

# Get curr. US Central
central = pytz.timezone('US/Central')
now = datetime.now(central)
file_name = now.strftime("%Y-%m-%d_%H-%M-%S") + ".csv"


file_path = '../API_data/'

# Check if the directory exists! --- else it will never work LOL
if not os.path.exists(file_path):
    os.makedirs(file_path)

# need full file path, here combine
full_file_path = os.path.join(file_path, file_name)

# Save it
df.to_csv(full_file_path, index=False)
