from django.shortcuts import render
import requests
import json
from newsapi import NewsApiClient

# Create your views here.
#api_key = 70c200a5636c44e69a93e7816b8eaf77
newsapi = NewsApiClient(api_key='70c200a5636c44e69a93e7816b8eaf77')
print(newsapi)

choices = {
    'ABC':'abc-news',
    'BBC':'bbc-news',
    'CNN':'cnn',
    'TOI':'the-times-of-india',
    'Hindu':'the-hindu',
    'Google':'google-news-in',
    'NYTimes':'the-new-york-times',
}

top_headlines_all = newsapi.get_top_headlines(
                                          sources='abc-news,bbc-news,the-times-of-india,the-hindu,google-news-in',
                                          language='en',
                                         )
# print(top_headlines_all)

all_articles = newsapi.get_everything(
                                      sources='bbc-news',

                                      language='en',
                                      sort_by='relevancy',)


# print(all_articles)
url_top = ("https://newsapi.org/v2/top-headlines?country=in&apiKey=70c200a5636c44e69a93e7816b8eaf77")

url_toi = ( "https://newsapi.org/v2/top-headlines?source=the-times-of-india&apiKey=70c200a5636c44e69a93e7816b8eaf77" )
url_cnn = ("https://newsapi.org/v2/top-headlines?source=cnn&apiKey=70c200a5636c44e69a93e7816b8eaf77")
url_bbc = ("https://newsapi.org/v2/top-headlines?source=bbc-news&apiKey=70c200a5636c44e69a93e7816b8eaf77")
url_hindu = ("https://newsapi.org/v2/top-headlines?source=the-hindu&apiKey=70c200a5636c44e69a93e7816b8eaf77")
url_google = ("https://newsapi.org/v2/top-headlines?source=google-news-in&apiKey=70c200a5636c44e69a93e7816b8eaf77")




response = requests.get(url_top)
# response_toi = requests.get(url_toi).json()
# response_cnn = requests.get(url_cnn).json()
# response_bbc = requests.get(url_bbc).json()
# response_hindu = requests.get(url_hindu).json()
# response_google = requests.get(url_google).json()
# data_toi = response_toi['articles']
# data_cnn = response_cnn['articles']
# data_bbc = response_bbc['articles']
# data_hindu = response_hindu['articles']
# data_google = response_google['articles']


url_cat = ()
news = response.json()
data = news['articles']
# print(data)
source = []
title = []
description = []
content = []
img_url = []
pubish_date = []

def home(request):
    template = "posts/home.html"

    context = {
        # 'source': source,
        # 'content':content,
        # 'title':title,
        # 'img_url':img_url,
        # 'publish_date':pubish_date,
        # 'description':description,
        'data':data,
    }

    return render(request,template,context)

def post(request):
    template = 'posts/index.html'
    context = {
        'data':data,
    }
    return render(request,template,context)


def sports(request):
    template = 'posts/sports.html'
    url_sport = ('https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=70c200a5636c44e69a93e7816b8eaf77')
    response = requests.get(url_sport).json()
    context = {
    'sports':response['articles'],
    }
    # print(response)
    return render(request,template,context)


def top_articles(request):
    template = 'posts/top.html'

    context = {
        'data':top_headlines_all['articles'],
    }
    # for x in top_headlines_all:
    #     print(top_headlines_all['title'])
    # print(top_headlines_all)
    return render(request, template, context)

def tech(request):
    template = 'posts/tech.html'
    url_sport = ('https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=70c200a5636c44e69a93e7816b8eaf77')
    response = requests.get(url_sport).json()
    context = {
    'techs':response['articles'],
    }
    # print(response)
    return render(request,template,context)

def business(request):
    template = 'posts/business.html'
    url_sport = ('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=70c200a5636c44e69a93e7816b8eaf77')
    response = requests.get(url_sport).json()
    context = {
    'business':response['articles'],
    }
    # print(response)
    return render(request,template,context)

def entertain(request):
    template = 'posts/entertain.html'
    url_sport = ('https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=70c200a5636c44e69a93e7816b8eaf77')
    response = requests.get(url_sport).json()
    context = {
    'entertain':response['articles'],
    }
    # print(response)
    return render(request,template,context)


def health(request):
    template = 'posts/business.html'
    url_sport = ('https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=70c200a5636c44e69a93e7816b8eaf77')
    response = requests.get(url_sport).json()
    context = {
    'health':response['articles'],
    }
    # print(response)
    return render(request,template,context)

