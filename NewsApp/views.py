from django.shortcuts import render
from newsapi import NewsApiClient
from django.views.decorators.cache import cache_page

@cache_page(60*60*24)
def index(request):
    newsapi = NewsApiClient(api_key="d82ee41695e140d78c1726d37ae3a703")
    topheadlines = newsapi.get_top_headlines(sources='TechRadar,techcrunch,wired,engadget,the-next-web,the-verge')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'index.html', context={"mylist":mylist})


@cache_page(60*60*24)
def TechRadar(request):
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources='TechRadar')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'TechRadar.html', context={"mylist":mylist})


@cache_page(60*60*24)
def techcrunch(request):
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources='techcrunch')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'techcrunch.html', context={"mylist":mylist})
#google-news,engadget,business-insider,wired,the-times-of-india,techcrunch,the-verge,the-next-web
@cache_page(60*60*24)
def wired(request):
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources='wired')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'wired.html', context={"mylist":mylist})

@cache_page(60*60*24)
def theverge(request):
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources='the-verge')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'theverge.html', context={"mylist":mylist})

@cache_page(60*60*24)
def thenextweb(request):
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources='the-next-web')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'thenextweb.html', context={"mylist":mylist})

@cache_page(60*60*24)
def engadget(request):
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources='engadget')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'engadget.html', context={"mylist":mylist})
