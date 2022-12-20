from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    
    
    return render(request, 'mysite/index.html')

