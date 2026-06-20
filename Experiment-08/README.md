# Experiment-08: Register Admin Interfaces for Student and Course Models, Perform Migrations, and Illustrate Data Entry Through Admin Forms

## Aim

To register the Course and Student models from the student-course registration app in the Django admin interface using custom admin classes, perform database migrations, create a superuser, and demonstrate data entry through the admin forms.

## Prerequisites

* Python 3.x installed
* Django installed
* Visual Studio Code available
* Virtual environment workflow understood from previous experiments
* Understanding of Django models from Experiment-07

## Folder Contents

```
Experiment-08/
├── README.md
└── project_files/
    └── student_course_admin_project/
        ├── manage.py
        ├── student_course_admin_project/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── student_course_registration_app/
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── models.py
            ├── tests.py
            ├── views.py
            └── migrations/
                └── __init__.py
```

## Step-by-Step Procedure

### Step 1: Create Django Project

```bash
django-admin startproject student_course_admin_project
```

### Step 2: Navigate into Project Directory and Create App

```bash
cd student_course_admin_project
python manage.py startapp student_course_registration_app
```

### Step 3: Add App to INSTALLED_APPS

In `student_course_admin_project/settings.py`, add:

```python
'student_course_registration_app',
```

### Step 4: Create Models

File: `student_course_registration_app/models.py`

```python
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True, default='')
    courses = models.ManyToManyField(Course, related_name='students', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

### Step 5: Register Models in Admin with Custom Admin Classes

File: `student_course_registration_app/admin.py`

```python
from django.contrib import admin
from .models import Course, Student

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    filter_horizontal = ('courses',)
```

This uses decorators to register models with custom `ModelAdmin` classes:
* `CourseAdmin` displays `name` and `description` columns in the list view
* `StudentAdmin` displays `first_name`, `last_name`, and `email` columns, and uses a horizontal filter widget for the `courses` many-to-many field

### Step 6: Make Migrations

```bash
python manage.py makemigrations
```

### Step 7: Apply Migrations

```bash
python manage.py migrate
```

### Step 8: Create Superuser

```bash
python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password. For example:

* Username: `admin`
* Password: `1234`

(You may choose your own credentials.)

### Step 9: Run Development Server

```bash
python manage.py runserver
```

### Step 10: Access Admin Interface

Open your browser and go to:

```
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials created in Step 8.

### Step 11: Add Data Through Admin Forms

Once logged in, you will see the admin dashboard with sections for:
* **Groups** and **Users** (default Django auth models)
* **Courses** and **Students** (from the app)

**Adding a Course:**
1. Click "Add" next to Courses
2. Enter the course name and description
3. Click "Save"

**Adding a Student:**
1. Click "Add" next to Students
2. Enter first name, last name, and email
3. Select courses from the available list (using the horizontal filter interface)
4. Click "Save"

Students and Courses can also be edited, filtered, searched, and deleted through the admin interface.

## Commands Used

| Step | Command |
|------|---------|
| Create project | `django-admin startproject student_course_admin_project` |
| Enter project | `cd student_course_admin_project` |
| Create app | `python manage.py startapp student_course_registration_app` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Create superuser | `python manage.py createsuperuser` |
| Run server | `python manage.py runserver` |

## File Explanations

| File | Purpose |
|------|---------|
| `manage.py` | Django's command-line utility for administrative tasks |
| `student_course_admin_project/settings.py` | Project settings including installed apps, database, templates |
| `student_course_admin_project/urls.py` | Root URL configuration; only admin route is registered |
| `student_course_registration_app/models.py` | Defines `Course` and `Student` models with ManyToMany relationship |
| `student_course_registration_app/admin.py` | Registers models in admin with custom `ModelAdmin` classes, `list_display`, and `filter_horizontal` |

## Expected Output

After running `python manage.py runserver` and logging into `http://127.0.0.1:8000/admin/`:

* **Course** and **Student** models appear in the admin dashboard under the app section
* Course list view shows `name` and `description` columns
* Student list view shows `first_name`, `last_name`, and `email` columns
* The `courses` field in the Student form is displayed using the horizontal filter widget for easy multi-selection
* Courses can be added, edited, deleted, and searched through the admin interface
* Students can be added, edited, deleted, and searched through the admin interface

## Conclusion

This experiment demonstrates how to register Django models in the admin interface using custom `ModelAdmin` classes with the `@admin.register()` decorator. Key configuration options include `list_display` to control which fields appear in the list view and `filter_horizontal` to provide a user-friendly multi-select widget for many-to-many fields. The admin interface provides a complete CRUD (Create, Read, Update, Delete) interface for managing application data without writing custom forms or views.

## Notes

* Activate the virtual environment before running Django commands
* Run `python manage.py makemigrations` before `migrate` since new models are created
* Superuser credentials should be kept secure in production
* Passwords must meet Django's minimum length requirements (unless running with `--skip-checks`)
* A complete runnable project snapshot is stored in `project_files/`
