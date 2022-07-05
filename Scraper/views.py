from django.shortcuts import render
from newsapi import NewsApiClient
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
@cache_page(60*60*24)
def index(request):
    newsapi = NewsApiClient(api_key="d82ee41695e140d78c1726d37ae3a703")
    topheadlines = newsapi.get_top_headlines()
    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        a = articles[i]

        news.append(a['title'])
        desc.append(a['description'])
        img.append(a['urlToImage'])
        url.append(a['url'])


    mylist = zip(news, desc, img, url)


    return render(request, 'index.html', context={"mylist": mylist})


