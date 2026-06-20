# Experiment-05: Develop a Simple Django App that Displays an Unordered List of Fruits and Ordered List of Selected Students

## Aim

To create a Django application that displays an unordered list of fruits and an ordered list of selected students for an event.

## Prerequisites

* Python 3.x installed
* Django installed
* Visual Studio Code available
* Virtual environment workflow understood from previous experiments

## Folder Contents

```
Experiment-05/
├── README.md
└── project_files/
    └── listfruit_project/
        ├── manage.py
        ├── listfruit_project/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── listfruit_app/
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
                └── listfruit_app/
                    └── fruits_student.html
```

## Step-by-Step Procedure

### Step 1: Create Django Project

```bash
django-admin startproject listfruit_project
```

### Step 2: Navigate into Project Directory and Create App

```bash
cd listfruit_project
python manage.py startapp listfruit_app
```

### Step 3: Write the View

File: `listfruit_app/views.py`

```python
from django.shortcuts import render

def fruit_student(request):
    fruitList = ['Mango', 'Kiwi', 'Banana', 'Apple', 'Grapes']
    studentList = ['Rama', 'Chetan', 'Kumar', 'Harish', 'Geetha']

    context = {
        'fruitList': fruitList,
        'studentList': sorted(studentList),
    }
    return render(request, 'listfruit_app/fruits_student.html', context)
```

### Step 4: Create the Template

Create:
`listfruit_app/templates/listfruit_app/fruits_student.html`

```html
<!DOCTYPE html>
<html>
<head>
<style>
#a1 { background-color: lightblue; color: brown; }
#a2 { background-color: blue; color: yellow; }
</style>
<title>Unordered Fruits and Ordered Students</title>
</head>
<body>
    <h1 id="a1">Unordered List of Fruits</h1>
    <ul>
        {% for fruit in fruitList %}
            <li>{{ fruit }}</li>
        {% endfor %}
    </ul>

    <h1 id="a2">Ordered List of Students Selected for an Event</h1>
    <ol>
        {% for student in studentList %}
            <li>{{ student }}</li>
        {% endfor %}
    </ol>
</body>
</html>
```

### Step 5: Create App-Level URL Configuration

File: `listfruit_app/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('fruits/', views.fruit_student, name='fruit_student'),
]
```

### Step 6: Add App to INSTALLED_APPS

In `listfruit_project/settings.py`, add:

```python
'listfruit_app',
```

### Step 7: Include App URLs in Project URL Configuration

File: `listfruit_project/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('listfruit_app.urls')),
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
`http://127.0.0.1:8000/fruits/`

## Commands Used

| Step | Command |
|------|---------|
| Create project | `django-admin startproject listfruit_project` |
| Enter project | `cd listfruit_project` |
| Create app | `python manage.py startapp listfruit_app` |
| Apply migrations | `python manage.py migrate` |
| Run server | `python manage.py runserver` |

## File Explanations

| File | Purpose |
|------|---------|
| `manage.py` | Django's command-line utility for administrative tasks |
| `listfruit_project/settings.py` | Project settings including installed apps, database, templates |
| `listfruit_project/urls.py` | Root URL configuration; includes app URLs |
| `listfruit_app/views.py` | Contains the `fruit_student` view function that defines lists and passes them to the template |
| `listfruit_app/urls.py` | App-level URL routing; maps `/fruits/` to the view |
| `listfruit_app/templates/listfruit_app/fruits_student.html` | HTML template displaying unordered fruit list and ordered student list |

## Expected Output

After running `python manage.py runserver`, open:

```
http://127.0.0.1:8000/fruits/
```

The browser should display:

* **Unordered List of Fruits** – Mango, Kiwi, Banana, Apple, Grapes
* **Ordered List of Students Selected for an Event** – Chetan, Geetha, Harish, Kumar, Rama (sorted alphabetically)

## Conclusion

This Django application successfully demonstrates passing Python lists from a view to a template and rendering them using Django template loops (`{% for %}`). The fruit list is displayed as an unordered list and the sorted student list as an ordered list.

## Notes

* Activate the virtual environment before running Django commands
* If the server does not run, verify Django installation
* The student list is sorted alphabetically using Python's `sorted()` before being passed to the template
* A complete runnable project snapshot is stored in `project_files/`
