from django.shortcuts import render
from newsapi import NewsApiClient
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
@cache_page(60*60*24)
def index(request, src):
    newsapi = NewsApiClient(api_key="d82ee41695e140d78c1726d37ae3a703")
    topheadlines = newsapi.get_top_headlines(source = src)
    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        article = articles[i]

        news.append(article['title'])
        desc.append(article['description'])
        img.append(article['urlToImage'])
        url.append(article['url'])


    mylist = zip(news, desc, img, url)


    return render(request, 'index.html', context={"mylist": mylist})


