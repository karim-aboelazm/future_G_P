# from newsdataapi import NewsDataApiClient

# # API key authorization, Initialize the client with your API key

# api = NewsDataApiClient(api_key="pub_5884911e7278f6d622745f1357e35b80955e")

# # You can pass empty or with request parameters {ex. (country = "us")}

import requests

data = requests.get("https://newsdata.io/api/1/news?apikey=pub_5884911e7278f6d622745f1357e35b80955e&language=en")


response = data.json()
news = response['results'][0]
# for new in news:
#     print(new['title'])
# # print(new['title'],"\n",new['full_description'][:100])
print(news['title'])