# Experiment-04: Develop a Django App that Displays Date and Time Four Hours Ahead and Four Hours Before

## Aim

To create a Django application that displays the current server date and time along with values four hours ahead and four hours before.

## Prerequisites

* Python 3.x installed
* Django installed
* Visual Studio Code available
* Virtual environment workflow understood from previous experiments

## Folder Contents

```
Experiment-04/
├── README.md
└── project_files/
    └── fourdatetime_project/
        ├── manage.py
        ├── fourdatetime_project/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── fourdatetime_app/
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
                └── fourdatetime_app/
                    └── datetime_offsets.html
```

## Step-by-Step Procedure

### Step 1: Create Django Project

```bash
django-admin startproject fourdatetime_project
```

### Step 2: Navigate into Project Directory and Create App

```bash
cd fourdatetime_project
python manage.py startapp fourdatetime_app
```

### Step 3: Write the View

File: `fourdatetime_app/views.py`

```python
from django.shortcuts import render
import datetime

def datetime_offsets(request):
    now = datetime.datetime.now()
    context = {
        'current_datetime': now,
        'four_hours_ahead': now + datetime.timedelta(hours=4),
        'four_hours_before': now - datetime.timedelta(hours=4),
    }
    return render(request, 'fourdatetime_app/datetime_offsets.html', context)
```

### Step 4: Create the Template

Create:
`fourdatetime_app/templates/fourdatetime_app/datetime_offsets.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Current date and time</title>
</head>
<body>
    <h1>Current Date and Time on the Server</h1>
    <p>{{ current_datetime }}</p>

    <h2>Four Hours Ahead</h2>
    <p>{{ four_hours_ahead }}</p>

    <h2>Four Hours Before</h2>
    <p>{{ four_hours_before }}</p>
</body>
</html>
```

### Step 5: Create App-Level URL Configuration

File: `fourdatetime_app/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('datetime-offsets/', views.datetime_offsets, name='datetime_offsets'),
]
```

### Step 6: Add App to INSTALLED_APPS

In `fourdatetime_project/settings.py`, add:

```python
'fourdatetime_app',
```

### Step 7: Include App URLs in Project URL Configuration

File: `fourdatetime_project/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fourdatetime_app.urls')),
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
`http://127.0.0.1:8000/datetime-offsets/`

## Commands Used

| Step | Command |
|------|---------|
| Create project | `django-admin startproject fourdatetime_project` |
| Enter project | `cd fourdatetime_project` |
| Create app | `python manage.py startapp fourdatetime_app` |
| Apply migrations | `python manage.py migrate` |
| Run server | `python manage.py runserver` |

## File Explanations

| File | Purpose |
|------|---------|
| `manage.py` | Django's command-line utility for administrative tasks |
| `fourdatetime_project/settings.py` | Project settings including installed apps, database, templates |
| `fourdatetime_project/urls.py` | Root URL configuration; includes app URLs |
| `fourdatetime_app/views.py` | Contains the `datetime_offsets` view function |
| `fourdatetime_app/urls.py` | App-level URL routing; maps `/datetime-offsets/` to the view |
| `fourdatetime_app/templates/fourdatetime_app/datetime_offsets.html` | HTML template displaying current, ahead, and before times |

## Expected Output

After running `python manage.py runserver`, open:

```
http://127.0.0.1:8000/datetime-offsets/
```

The browser should display:

* **Current Date and Time on the Server** – current server date and time
* **Four Hours Ahead** – date and time four hours from now
* **Four Hours Before** – date and time four hours before now

## Conclusion

This Django application successfully calculates and displays time offsets relative to the current server time. The experiment demonstrates the use of the `datetime` module with `timedelta` for time arithmetic, along with Django views, URL routing, and template rendering.

## Notes

* Activate the virtual environment before running Django commands
* If the server does not run, verify Django installation
* The displayed time depends on the server environment / timezone setting
* A complete runnable project snapshot is stored in `project_files/`
