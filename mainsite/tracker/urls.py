from django.urls import path

from . import views

app_name = "tracker"

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("create", views.create_view, name="create"),
    path("<int:pk>", views.DetailView.as_view(), name="detail")
]