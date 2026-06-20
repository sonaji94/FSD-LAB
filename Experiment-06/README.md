# Experiment-06: Develop a Layout Template with Navigation and Footer, and Create Home, About Us and Contact Us Pages Using Template Inheritance

## Aim

To create a Django application using a base layout template with navigation and footer, and to create Home, About Us, and Contact Us pages by inheriting the layout.

## Prerequisites

* Python 3.x installed
* Django installed
* Visual Studio Code available
* Virtual environment workflow understood from previous experiments

## Folder Contents

```
Experiment-06/
├── README.md
└── project_files/
    └── portfolio_project/
        ├── manage.py
        ├── portfolio_project/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── portfolioapp/
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
                └── portfolioapp/
                    ├── layout.html
                    ├── home.html
                    ├── about.html
                    └── contactus.html
```

## Step-by-Step Procedure

### Step 1: Create Django Project

```bash
django-admin startproject portfolio_project
```

### Step 2: Navigate into Project Directory and Create App

```bash
cd portfolio_project
python manage.py startapp portfolioapp
```

### Step 3: Add App to INSTALLED_APPS

In `portfolio_project/settings.py`, add:

```python
'portfolioapp',
```

### Step 4: Create the Base Layout Template

Create:
`portfolioapp/templates/portfolioapp/layout.html`

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        nav { background-color: lightblue; padding: 15px; }
        nav a { margin-right: 15px; text-decoration: none; }
    </style>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'main' %}">HOME</a>
        <a href="{% url 'contact' %}">CONTACT US</a>
        <a href="{% url 'about' %}">ABOUT US</a>
    </nav>

    <section>
        {% block content %}{% endblock %}
    </section>

    <footer>
        <hr>
        &copy; Designed and Developed by CSD Department FETC, SUK Kalburgi.
    </footer>
</body>
</html>
```

### Step 5: Create the Home Page Template

Create:
`portfolioapp/templates/portfolioapp/home.html`

```html
{% extends 'portfolioapp/layout.html' %}

{% block title %}HOME Page{% endblock %}

{% block content %}
<h1>This is my home page</h1>
{% endblock %}
```

### Step 6: Create the About Us Template

Create:
`portfolioapp/templates/portfolioapp/about.html`

```html
{% extends 'portfolioapp/layout.html' %}

{% block title %}ABOUT PAGE{% endblock %}

{% block content %}
<h1>About Us</h1>
<p>CSD Department FETC SUK KLB</p>
{% endblock %}
```

### Step 7: Create the Contact Us Template

Create:
`portfolioapp/templates/portfolioapp/contactus.html`

```html
{% extends 'portfolioapp/layout.html' %}

{% block title %}Contact us{% endblock %}

{% block content %}
<h1>Contact us</h1>
<p>Name: Sharanabasappa Noola</p>
<p>Designation: Asst. Prof</p>
<p>Mobile: 8523697412</p>
<p>Email: abc@gmail.com</p>
{% endblock %}
```

### Step 8: Write the Views

File: `portfolioapp/views.py`

```python
from django.shortcuts import render

def main(request):
    return render(request, 'portfolioapp/home.html')

def about(request):
    return render(request, 'portfolioapp/about.html')

def contact(request):
    return render(request, 'portfolioapp/contactus.html')
```

### Step 9: Create App-Level URL Configuration

File: `portfolioapp/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

### Step 10: Include App URLs in Project URL Configuration

File: `portfolio_project/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolioapp.urls')),
]
```

### Step 11: Apply Migrations

```bash
python manage.py migrate
```

### Step 12: Run the Development Server

```bash
python manage.py runserver
```

Open the following URLs:

* `http://127.0.0.1:8000/main/`
* `http://127.0.0.1:8000/about/`
* `http://127.0.0.1:8000/contact/`

## Commands Used

| Step | Command |
|------|---------|
| Create project | `django-admin startproject portfolio_project` |
| Enter project | `cd portfolio_project` |
| Create app | `python manage.py startapp portfolioapp` |
| Apply migrations | `python manage.py migrate` |
| Run server | `python manage.py runserver` |

## File Explanations

| File | Purpose |
|------|---------|
| `manage.py` | Django's command-line utility for administrative tasks |
| `portfolio_project/settings.py` | Project settings including installed apps, database, templates |
| `portfolio_project/urls.py` | Root URL configuration; includes app URLs |
| `portfolioapp/views.py` | Contains `main`, `about`, and `contact` view functions |
| `portfolioapp/urls.py` | App-level URL routing for `/main/`, `/about/`, `/contact/` |
| `portfolioapp/templates/portfolioapp/layout.html` | Base layout template with navigation and footer |
| `portfolioapp/templates/portfolioapp/home.html` | Home page extending layout.html |
| `portfolioapp/templates/portfolioapp/about.html` | About Us page extending layout.html |
| `portfolioapp/templates/portfolioapp/contactus.html` | Contact Us page extending layout.html |

## Expected Output

After running `python manage.py runserver`:

* `http://127.0.0.1:8000/main/` – displays the Home page with navigation and footer
* `http://127.0.0.1:8000/about/` – displays the About Us page with navigation and footer
* `http://127.0.0.1:8000/contact/` – displays the Contact Us page with navigation and footer

All pages share the common layout template with navigation menu and copyright footer.

## Conclusion

This Django application demonstrates template inheritance by creating a reusable base layout template (`layout.html`) with a navigation menu and footer, and then creating three child pages (Home, About Us, Contact Us) that extend the layout. The navigation links use Django's `{% url %}` tag to route between pages.

## Notes

* Activate the virtual environment before running Django commands
* If the server does not run, verify Django installation
* Navigation links use Django's `{% url %}` template tag with named URL patterns
* A complete runnable project snapshot is stored in `project_files/`
