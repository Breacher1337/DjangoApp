from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, Http404

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
        result = "No page for that topic"
        return Http404("Generic Error")

def add_view(request, num1,num2):

    result = num1 + num2
    result = f"{num1} + {num2} = {result}"
    return HttpResponse(str(result))

        