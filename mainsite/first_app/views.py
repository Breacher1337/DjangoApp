from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def simple_view(request):
    return HttpResponse("Hello, world.")