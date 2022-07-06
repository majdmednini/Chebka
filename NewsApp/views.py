from django.shortcuts import render
from newsapi import NewsApiClient
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods

#permit only get methods to prevent http header attacks 
@require_http_methods(["GET"])
#cache the page for a day in seconds
#updating the content will be done through django-apsscheuler
@cache_page(60*60*24)
#make the app adaptive to user needs
def index(request, src):
    newsapi = NewsApiClient(api_key="d82ee41695e140d78c1726d37ae3a703")
    topheadlines = newsapi.get_top_headlines(source = src)
    #get only the artciles without the other metadata
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

    #make a list of lists and this is the tighr syntax to  do it
    #using zip method for faster rendering time
    #might use itertools for next features and zip two lists
    #that needs a differnet syntax
    mylist = zip(news, desc, img, url)


    return render(request, 'index.html', context={"mylist": mylist})


