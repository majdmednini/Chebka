#!/usr/bin/python3
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key="d82ee41695e140d78c1726d37ae3a703")
topheadlines = newsapi.get_top_headlines()
print(topheadlines)
