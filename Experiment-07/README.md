# Experiment-07: Develop a Django App that Performs Student Registration to a Course and Displays Students Registered for a Selected Course

## Aim

To create a Django application that manages student registration to courses using a ManyToMany relationship, and displays the list of students registered for any selected course.

## Prerequisites

* Python 3.x installed
* Django installed
* Visual Studio Code available
* Virtual environment workflow understood from previous experiments

## Folder Contents

```
Experiment-07/
├── README.md
└── project_files/
    └── student_course_project/
        ├── manage.py
        ├── student_course_project/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── student_course_registration_app/
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── forms.py
            ├── models.py
            ├── tests.py
            ├── views.py
            ├── urls.py
            ├── migrations/
            │   └── __init__.py
            └── templates/
                ├── base.html
                └── registration/
                    ├── index.html
                    ├── register_student.html
                    ├── register_course.html
                    └── student_list.html
```

## Step-by-Step Procedure

### Step 1: Create Django Project

```bash
django-admin startproject student_course_project
```

### Step 2: Navigate into Project Directory and Create App

```bash
cd student_course_project
python manage.py startapp student_course_registration_app
```

### Step 3: Add App to INSTALLED_APPS

In `student_course_project/settings.py`, add:

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

### Step 5: Register Models in Admin

File: `student_course_registration_app/admin.py`

```python
from django.contrib import admin
from .models import Course, Student

admin.site.register(Course)
admin.site.register(Student)
```

### Step 6: Create Forms

File: `student_course_registration_app/forms.py`

```python
from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'courses']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'courses': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
```

### Step 7: Create Views

File: `student_course_registration_app/views.py`

```python
from django.shortcuts import render, redirect
from .models import Course, Student
from .forms import StudentForm, CourseForm

def index(request):
    courses = Course.objects.all()
    return render(request, 'registration/index.html', {'courses': courses})

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'registration/register_student.html', {'form': form})

def register_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'registration/register_course.html', {'form': form})

def student_list(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.students.all()
    return render(request, 'registration/student_list.html', {'students': students, 'course': course})
```

### Step 8: Create Templates

#### `templates/base.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Student Registration</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

#### `templates/registration/index.html`

```html
{% extends 'base.html' %}
{% block content %}
<div class="container">
    <h1 class="mt-5">Courses</h1>
    <ul class="list-group mt-3">
        {% for course in courses %}
            <li class="list-group-item">
                <a href="{% url 'student_list' course.id %}">{{ course.name }}</a>
            </li>
        {% endfor %}
    </ul>

    <a class="btn btn-primary mt-3" href="{% url 'register_student' %}">Register Student</a>
    <a class="btn btn-secondary mt-3" href="{% url 'register_course' %}">Register Course</a>
</div>
{% endblock %}
```

#### `templates/registration/register_student.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container">
    <h1>Register Student</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Register</button>
    </form>
</div>
</body>
</html>
```

#### `templates/registration/register_course.html`

```html
{% extends 'base.html' %}
{% block content %}
<h1>Register Course</h1>
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <form method="post">
                {% csrf_token %}
                {% for field in form %}
                    <div class="form-group">
                        {{ field.label_tag }}
                        {{ field }}
                        {% if field.help_text %}
                            <small class="form-text text-muted">{{ field.help_text }}</small>
                        {% endif %}
                        {% for error in field.errors %}
                            <div class="alert alert-danger">{{ error }}</div>
                        {% endfor %}
                    </div>
                {% endfor %}
                <button type="submit" class="btn btn-primary">Register</button>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```

#### `templates/registration/student_list.html`

```html
{% extends 'base.html' %}
{% block content %}
<h1>Students Registered for {{ course.name }}</h1>
<ul>
    {% for student in students %}
        <li>{{ student.first_name }} {{ student.last_name }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

### Step 9: Create App-Level URL Configuration

File: `student_course_registration_app/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register-student/', views.register_student, name='register_student'),
    path('register-course/', views.register_course, name='register_course'),
    path('student-list/<int:course_id>/', views.student_list, name='student_list'),
]
```

### Step 10: Include App URLs in Project URL Configuration

File: `student_course_project/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_course_registration_app.urls')),
]
```

### Step 11: Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 12: Run the Development Server

```bash
python manage.py runserver
```

Open:

* `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/index/`

## Commands Used

| Step | Command |
|------|---------|
| Create project | `django-admin startproject student_course_project` |
| Enter project | `cd student_course_project` |
| Create app | `python manage.py startapp student_course_registration_app` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Run server | `python manage.py runserver` |

## File Explanations

| File | Purpose |
|------|---------|
| `manage.py` | Django's command-line utility for administrative tasks |
| `student_course_project/settings.py` | Project settings including installed apps, database, templates |
| `student_course_project/urls.py` | Root URL configuration; includes app URLs |
| `student_course_registration_app/models.py` | Defines `Course` and `Student` models with ManyToMany relationship |
| `student_course_registration_app/forms.py` | Model forms for `Student` and `Course` |
| `student_course_registration_app/views.py` | Contains `index`, `register_student`, `register_course`, and `student_list` views |
| `student_course_registration_app/urls.py` | App-level URL routing |
| `student_course_registration_app/admin.py` | Registers models in Django admin |
| `templates/base.html` | Base template |
| `templates/registration/index.html` | Course listing page |
| `templates/registration/register_student.html` | Student registration form |
| `templates/registration/register_course.html` | Course registration form |
| `templates/registration/student_list.html` | Students registered for a selected course |

## Expected Output

After running `python manage.py runserver`:

* `http://127.0.0.1:8000/index/` – shows a list of courses with links to view registered students, plus buttons to register a student or course
* Clicking a course name shows the students registered for that course
* "Register Student" form allows creating a new student and selecting multiple courses
* "Register Course" form allows creating a new course

## Conclusion

This Django application demonstrates a ManyToMany relationship between Student and Course models. Students can be registered to multiple courses, and the application displays the list of students registered for any selected course. The experiment covers models, forms, views, templates, URL routing, and the Django admin interface.

## Notes

* Activate the virtual environment before running Django commands
* Run `python manage.py makemigrations` before `migrate` since new models are created
* Create a superuser with `python manage.py createsuperuser` to access the admin interface at `/admin/`
* A complete runnable project snapshot is stored in `project_files/`
