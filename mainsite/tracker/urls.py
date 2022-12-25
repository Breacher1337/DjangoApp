from django.urls import path

from . import views

app_name = "tracker"

urlpatterns = [
    path("", views.home_view, name="index"),
    path("create", views.create_view, name="create")
]