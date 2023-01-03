from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):

    mode = "quotes"
    response = requests.get(f"https://zenquotes.io/api/{mode}?option1=value&option2=value")

    print(response.text)

    data = response.text

    

    return render(request, 'mysite/index.html')

