# Experiment-02: Creation of Virtual Environment, Django Project and App

---

## Aim

To demonstrate the creation of a Python virtual environment, installation of Django, creation of a Django project and app, addition of the app to `INSTALLED_APPS`, running migrations, and starting the Django development server.

---

## Prerequisites

- Python 3.x installed (verified in Experiment-01)
- Visual Studio Code installed
- Basic terminal / command prompt knowledge
- pip available

---

## Folder Contents

```
Experiment-02/
├── README.md
└── project_files/
    └── myproject/
        ├── manage.py
        ├── myproject/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── myapp/
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── migrations/
            │   └── __init__.py
            ├── models.py
            ├── tests.py
            └── views.py
```

---

## Step-by-Step Procedure

### Step 1: Open Visual Studio Code

Launch VS Code from the Start Menu (Windows) or using the terminal.

### Step 2: Create / Select a Project Folder

Create a new folder or open an existing one where you want to create the Django project.

### Step 3: Open Integrated Terminal

In VS Code, open the integrated terminal using `` Ctrl + ` `` (backtick) or by selecting **Terminal → New Terminal** from the menu.

### Step 4: Create a Virtual Environment

```bash
python -m venv env
```

This creates an isolated Python environment named `env` inside your project folder.

### Step 5: Activate the Virtual Environment

**Windows:**

```bash
env\Scripts\activate
```

**Linux / macOS:**

```bash
source env/bin/activate
```

Once activated, you will see `(env)` in your terminal prompt.

### Step 6: Install Django

```bash
pip install django
```

### Step 7: Create a Django Project

```bash
django-admin startproject myproject
```

This creates a `myproject/` directory with the default Django project structure.

### Step 8: Move into the Project Directory

```bash
cd myproject
```

### Step 9: Create a Django App

```bash
python manage.py startapp myapp
```

This creates a `myapp/` directory inside the project.

### Step 10: Add the App to INSTALLED_APPS

Open `myproject/settings.py` and add `'myapp'` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',          # <-- Add this line
]
```

### Step 11: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

This applies Django's default database migrations and creates the SQLite database file.

### Step 12: Run the Development Server

```bash
python manage.py runserver
```

---

## Commands Summary

| Step | Command |
|------|---------|
| Create virtual environment | `python -m venv env` |
| Activate (Windows) | `env\Scripts\activate` |
| Activate (Linux/macOS) | `source env/bin/activate` |
| Install Django | `pip install django` |
| Create project | `django-admin startproject myproject` |
| Enter project | `cd myproject` |
| Create app | `python manage.py startapp myapp` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Run server | `python manage.py runserver` |

---

## Project Structure Explanation

| File / Folder | Purpose |
|---------------|---------|
| `manage.py` | Django's command-line utility for administrative tasks |
| `myproject/` (project package) | Contains project-level settings and configuration |
| `myproject/__init__.py` | Marks the directory as a Python package |
| `myproject/settings.py` | Configuration file for the Django project |
| `myproject/urls.py` | URL declarations for the project |
| `myproject/asgi.py` | ASGI configuration for asynchronous server |
| `myproject/wsgi.py` | WSGI configuration for deployment |
| `myapp/` | The Django application package |
| `myapp/__init__.py` | Marks the directory as a Python package |
| `myapp/admin.py` | Admin interface configuration |
| `myapp/apps.py` | Application configuration |
| `myapp/models.py` | Database models (to be defined in later experiments) |
| `myapp/views.py` | View functions / classes (to be defined in later experiments) |
| `myapp/tests.py` | Test cases |
| `myapp/migrations/` | Database migration files |

---

## Expected Output

After running `python manage.py runserver`, open a web browser and go to:

```
http://127.0.0.1:8000/
```

You should see the **Django default welcome page** confirming that the project has been created successfully and the server is running.

---

## Conclusion

A Python virtual environment has been created, Django has been installed, a new Django project (`myproject`) and app (`myapp`) have been created, the app has been registered in `INSTALLED_APPS`, and the development server is running. This setup serves as the foundation for all subsequent Django experiments in this lab.

---

## Notes

- Always activate the virtual environment (`env`) before running any Django commands
- If Django is not found, ensure the virtual environment is activated and run `pip install django` or `pip install -r ../../requirements.txt`
- The virtual environment folder (`env/`) should not be committed to Git (already covered by `.gitignore`)
- In later experiments, we will build upon this project by adding models, views, templates, and more
- The `project_files/` directory contains a pre-built snapshot of the project for reference
