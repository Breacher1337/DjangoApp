from django.urls import path

from . import views

app_name = "tracker"

urlpatterns = [
    path("", views.home_view, name="index")
]