from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("list_of_places/", views.list_of_places, name="list_of_places"),
    path("add_new_place/", views.add_new_place, name="add_new_place"),
    path("place/<int:id>/", views.place_page, name="place_page"),
    path("random/", views.random_page, name="random_page"),
]
