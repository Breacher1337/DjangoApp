from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

articles = {
    "sports": "SPORTS PAGE",
    "finance": "FINANCE PAGE",
    "politics": "POLITICS PAGE"
}

def news_view(request,topic):
    try: 
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        return Http404("Generic Error")

def num_page_view(request,num_page):

    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    webpage = reverse("topic-page", args=[topic])

    return HttpResponseRedirect(webpage)

        