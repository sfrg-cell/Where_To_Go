# Where to Go

## Project Overview
"Where to Go" is a Django web application designed to help users manage a personalized list of locations and decide where to visit next. Instead of using a traditional database, this project utilizes Django Sessions to store data, making it an excellent example of session-based state management.

## Features
* **Add New Places:** A form-based interface to save place names, locations, types, ratings, and descriptions.
* **Place List:** A comprehensive view of all saved locations with visual star ratings.
* **Weighted Random Selection:** A "Random" feature that picks a place for you to visit. The higher the rating of a place, the higher the probability it will be chosen.
* **Detailed View:** Dedicated pages for each specific location to view full details and descriptions.
* **Session-based Storage:** Data is stored per user session, meaning no database configuration is required for local testing.

## Tech Stack
* **Framework:** Django 5.x
* **Language:** Python 3.x
* **Storage:** Django Session Framework

## Key Functionality
* **Dynamic Rating System:** Ratings are automatically converted into visual star icons (e.g., a rating of 5 becomes ⭐⭐⭐⭐⭐).
* **Smart Randomizer:** Uses the `random.choices` method with weights based on user ratings to prioritize better-rated locations in the selection process.

## URL Structure
The application uses the `app` namespace with the following routes:
* `/` or `/home/` — The landing page.
* `/add_new_place/` — Interface to add a new location to the session.
* `/list_of_places/` — A gallery/list of all added locations.
* `/place/<id>/` — Individual page for a specific location.
* `/random/` — Logic-driven redirect to a randomly selected place.


## How to run project

1. Create virtual env
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Apply migrations
```bash
python manage.py migrate
```
4. Run the server
```bash
python manage.py runserver
```

