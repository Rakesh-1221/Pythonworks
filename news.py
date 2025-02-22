"""import requests
from pprint import pprint

base_url="https://newsapi.org/v2/everything?"
api_key="134bc661eb3546c2b2678149e868650b"
news=input("Entet the title")
final_url=base_url + "q=" + news + "&apiKey=" + api_key
news_data=requests.get(final_url).json()
pprint(news_data)"""

import requests
from pprint import pprint

base_url = "https://newsapi.org/v2/top-headlines?"
api_key = "134bc661eb3546c2b2678149e868650b"
name = input("Entet the name of country")
final_url = base_url + "country=" + name + "&apiKey=" + api_key
news_data = requests.get(final_url).json()
pprint(news_data)
