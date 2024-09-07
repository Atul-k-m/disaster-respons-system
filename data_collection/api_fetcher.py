import requests
import json
from config import TWITTER_API_KEY, NEWS_API_KEY

# X (formerly Twitter) API Fetcher
import requests

# def fetch_x_data(query):
#   url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&tweet.fields=created_at,text"
#   headers = {"Authorization": f"Bearer {TWITTER_API_KEY}"}
  
#   try:
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()  # Raise an exception for non-2xx status codes
#     return response.json()
#   except requests.exceptions.HTTPError as e:
#     if e.response.status_code == 401:
#       # Handle authorization error
#       print("Error: Unauthorized access to Twitter API")
#       return None  # Or return a specific error object
#     else:
#       raise e  # Re-raise other HTTP errors

# News API Fetcher
def fetch_news_data(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}&pageSize=4"
    response = requests.get(url)
    return response.json()
