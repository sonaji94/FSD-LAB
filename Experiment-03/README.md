# Experiment-03: Develop a Django App that Displays Current Date and Time in Server

## Aim

To create a Django application that displays the current server date and time on a web page.

## Prerequisites

* Python 3.x installed
* Django installed
* Visual Studio Code available
* Virtual environment workflow understood from Experiment-01 and Experiment-02

## Folder Contents

```
Experiment-03/
├── README.md
└── project_files/
    └── datetime_project/
        ├── manage.py
        ├── datetime_project/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── datetime_app/
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── models.py
            ├── tests.py
            ├── views.py
            ├── urls.py
            ├── migrations/
            │   └── __init__.py
            └── templates/
                └── datetime_app/
                    └── current_datetime.html
```

## Step-by-Step Procedure

### Step 1: Create Django Project

```bash
django-admin startproject datetime_project
```

### Step 2: Navigate into Project Directory and Create App

```bash
cd datetime_project
python manage.py startapp datetime_app
```

### Step 3: Write the View

File: `datetime_app/views.py`

```python
from django.shortcuts import render
from django.utils import timezone

def current_datetime(request):
    now = timezone.now()
    context = {'datetime': now}
    return render(request, 'datetime_app/current_datetime.html', context)
```

### Step 4: Create the Template

Create:
`datetime_app/templates/datetime_app/current_datetime.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Current Date and Time</title>
</head>
<body>
    <h1>Current Date and Time</h1>
    <p>{{ datetime }}</p>
</body>
</html>
```

### Step 5: Create App-Level URL Configuration

File: `datetime_app/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_datetime, name='current_datetime'),
]
```

### Step 6: Add App to INSTALLED_APPS

In `datetime_project/settings.py`, add:

```python
'datetime_app',
```

### Step 7: Include App URLs in Project URL Configuration

File: `datetime_project/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('datetime_app.urls')),
]
```

### Step 8: Apply Migrations

```bash
python manage.py migrate
```

### Step 9: Run the Development Server

```bash
python manage.py runserver
```

Open:
`http://127.0.0.1:8000/`

## Commands Used

| Step | Command |
|------|---------|
| Create project | `django-admin startproject datetime_project` |
| Enter project | `cd datetime_project` |
| Create app | `python manage.py startapp datetime_app` |
| Apply migrations | `python manage.py migrate` |
| Run server | `python manage.py runserver` |

## File Explanations

| File | Purpose |
|------|---------|
| `manage.py` | Django's command-line utility for administrative tasks |
| `datetime_project/settings.py` | Project settings including installed apps, database, templates |
| `datetime_project/urls.py` | Root URL configuration; includes app URLs |
| `datetime_app/views.py` | Contains the `current_datetime` view function |
| `datetime_app/urls.py` | App-level URL routing; maps root path to the view |
| `datetime_app/templates/datetime_app/current_datetime.html` | HTML template that displays the date and time |

## Expected Output

After running `python manage.py runserver`, open:

```
http://127.0.0.1:8000/
```

The browser should display:

* heading: **Current Date and Time**
* current server date and time value

## Conclusion

This experiment demonstrates Django project creation, app creation, routing, views, templates, and displaying server date and time. The application successfully shows the current server date and time in the browser.

## Notes

* Activate the virtual environment before running Django commands
* If the server does not run, verify Django installation
* The displayed time depends on the server timezone setting (`TIME_ZONE` in `settings.py`)
* A complete runnable project snapshot is stored in `project_files/`
