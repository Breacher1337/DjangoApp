from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('simple_view', views.simple_view),
]