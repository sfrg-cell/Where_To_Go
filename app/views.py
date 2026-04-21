from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreatePlace
import datetime
import random


def home(request):
    return render(request, "app/home.html", {})


def add_new_place(request):
    if request.method == "POST":
        form = CreatePlace(request.POST)
        if form.is_valid():
            places = request.session.get("places", [])

            place_data = {
                "id": len(places) + 1,
                "name": form.cleaned_data["name"],
                "location": form.cleaned_data["location"],
                "place_type": form.cleaned_data["place_type"],
                "rating": int(form.cleaned_data["rating"]),
                "description": form.cleaned_data["description"],
                "created_at": str(datetime.date.today()),
            }

            place_data["stars"] = "⭐" * place_data["rating"]

            places.append(place_data)
            request.session["places"] = places

            return HttpResponseRedirect(reverse("app:list_of_places"))
    else:
        form = CreatePlace()
    return render(request, "app/add_new_place.html", {"form": form})


def list_of_places(request):
    places = request.session.get("places", [])
    return render(request, "app/list_of_places.html", {"places": places})


def place_page(request, id):
    places = request.session.get("places", [])
    place = next((p for p in places if p["id"] == int(id)), None)
    return render(request, "app/place_page.html", {"place": place})


def random_page(request):
    places = request.session.get("places", [])
    if not places:
        return render(request, "app/error.html")

    weights = [place["rating"] for place in places]
    chosen = random.choices(places, weights=weights, k=1)[0]

    return HttpResponseRedirect(reverse("app:place_page", args=[chosen["id"]]))
