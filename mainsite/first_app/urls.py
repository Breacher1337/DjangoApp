from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('<topic>/', views.news_view),
    path("<int:num1>/<int:num2>", views.add_view)
]