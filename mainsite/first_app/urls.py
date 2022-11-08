from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('<str:topic>/', views.news_view, name="topic-page"),
    path("<int:num_page>/", views.num_page_view)
]