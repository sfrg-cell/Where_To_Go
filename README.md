# Where To Go Project by Havryliuk Ioanna

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

## Endpoints

### Home
- `/` - main homepage
- `/home/` - also main homepage (redirects to `/`)

### Places
- `/list_of_places/` - list of all places
- `/add_new_place/` - add a new place via a form
- `/place/<int:id>/` - page of a specific place by its ID
- `/random/` - random place, weighted by rating
