# Experiment-09: Develop a Model Form for Student Project Details Using a Project Model

## Aim

To create a Django application that extends the student-course registration system by adding a Project model with a ModelForm, allowing students to be associated with projects having topic, languages used, and duration fields.

## Prerequisites

* Python 3.x installed
* Django installed
* Visual Studio Code available
* Virtual environment workflow understood from previous experiments
* Understanding of Django models, forms, views, and templates from Experiments 07-08

## Folder Contents

```
Experiment-09/
├── README.md
└── project_files/
    └── student_project_registration_project/
        ├── manage.py
        ├── student_project_registration_project/
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
                    ├── register_project.html
                    └── student_list.html
```

## Step-by-Step Procedure

### Step 1: Create Django Project

```bash
django-admin startproject student_project_registration_project
```

### Step 2: Navigate into Project Directory and Create App

```bash
cd student_project_registration_project
python manage.py startapp student_course_registration_app
```

### Step 3: Add App to INSTALLED_APPS

In `student_project_registration_project/settings.py`, add:

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

class Project(models.Model):
    topic = models.CharField(max_length=100, default='')
    languages_used = models.CharField(max_length=100, default='')
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.topic

class Student(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True, default='')
    courses = models.ManyToManyField(Course, related_name='students', blank=True)
    project = models.ManyToManyField(Project, related_name='students', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

A new `Project` model is added with `topic`, `languages_used`, and `duration` fields. The `Student` model now also includes a `project` ManyToMany field linking to the Project model.

### Step 5: Create Forms

File: `student_course_registration_app/forms.py`

```python
from django import forms
from .models import Student, Course, Project

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'courses', 'project']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'courses': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'project': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('topic', 'languages_used', 'duration')
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'languages_used': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
        }
```

The `ProjectForm` is a new ModelForm for the Project model. The `StudentForm` now also includes the `project` field for multi-selection.

### Step 6: Register Models in Admin

File: `student_course_registration_app/admin.py`

```python
from django.contrib import admin
from .models import Course, Student, Project

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Project)
```

### Step 7: Create Views

File: `student_course_registration_app/views.py`

```python
from django.shortcuts import render, redirect
from .models import Course, Student, Project
from .forms import StudentForm, CourseForm, ProjectForm

def index(request):
    courses = Course.objects.all()
    projects = Project.objects.all()
    return render(request, 'registration/index.html', {
        'courses': courses,
        'projects': projects,
    })

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

def register_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'registration/register_project.html', {'form': form})

def student_list(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.students.all()
    return render(request, 'registration/student_list.html', {'students': students, 'course': course})
```

The new `register_project` view handles project creation. The `index` view now passes both `courses` and `projects` to the template.

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
    <a class="btn btn-success mt-3" href="{% url 'register_project' %}">Register Project</a>

    <h1 class="mt-5 my-5">Projects</h1>
    <ul class="list-group mt-3">
        {% for project in projects %}
            <li class="list-group-item">
                {{ project.topic }}
            </li>
        {% endfor %}
    </ul>
</div>
{% endblock %}
```

#### `templates/registration/register_project.html`

```html
{% extends 'base.html' %}
{% block content %}
<div class="container my-3">
    <h1>Create Project</h1>
    <form method="post">
        {% csrf_token %}
        <div class="form-group">
            <label for="id_topic">Topic:</label>
            {{ form.topic }}
        </div>
        <div class="form-group">
            <label for="id_languages_used">Languages Used:</label>
            {{ form.languages_used }}
        </div>
        <div class="form-group">
            <label for="id_duration">Duration:</label>
            {{ form.duration }}
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
{% endblock %}
```

#### Other templates (`register_student.html`, `register_course.html`, `student_list.html`)

These follow the same structure as Experiment-07, with the student form now including project selection via `{{ form.as_p }}`.

### Step 9: Configure URLs

File: `student_course_registration_app/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register-student/', views.register_student, name='register_student'),
    path('register-course/', views.register_course, name='register_course'),
    path('projects_register/', views.register_project, name='register_project'),
    path('student-list/<int:course_id>/', views.student_list, name='student_list'),
]
```

File: `student_project_registration_project/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_course_registration_app.urls')),
]
```

### Step 10: Make Migrations

```bash
python manage.py makemigrations
```

### Step 11: Apply Migrations

```bash
python manage.py migrate
```

### Step 12: Run the Development Server

```bash
python manage.py runserver
```

### Step 13: Open in Browser

Navigate to:

```
http://127.0.0.1:8000/index/
```

## Commands Used

| Step | Command |
|------|---------|
| Create project | `django-admin startproject student_project_registration_project` |
| Enter project | `cd student_project_registration_project` |
| Create app | `python manage.py startapp student_course_registration_app` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Run server | `python manage.py runserver` |

## File Explanations

| File | Purpose |
|------|---------|
| `manage.py` | Django's command-line utility for administrative tasks |
| `student_project_registration_project/settings.py` | Project settings including installed apps, database, templates |
| `student_project_registration_project/urls.py` | Root URL configuration; includes app URLs and admin |
| `student_course_registration_app/models.py` | Defines `Course`, `Project`, and `Student` models |
| `student_course_registration_app/forms.py` | Model forms for `Student`, `Course`, and `Project` |
| `student_course_registration_app/views.py` | Contains `index`, `register_student`, `register_course`, `register_project`, and `student_list` views |
| `student_course_registration_app/urls.py` | App-level URL routing including `projects_register/` |
| `student_course_registration_app/admin.py` | Registers models in Django admin |
| `templates/registration/register_project.html` | Project creation form template |

## Expected Output

After running `python manage.py runserver` and navigating to `http://127.0.0.1:8000/index/`:

* The home page shows a list of courses and a list of projects
* "Register Student" form includes multi-select fields for both courses and projects
* "Register Course" form allows creating a new course
* "Register Project" form allows creating a new project with topic, languages used, and duration
* After creating a project, it appears in the projects list on the home page
* Clicking a course name shows the students registered for that course

## Conclusion

This experiment extends the student-course registration application by adding a Project model with a dedicated ModelForm. Students can now be associated with projects in addition to courses. The experiment demonstrates creating a new model, adding a ManyToMany relationship, creating a ModelForm, building a registration view and template, and updating the index page to display registered projects. This showcases how Django applications can be incrementally extended with new features.

## Notes

* Activate the virtual environment before running Django commands
* Run `python manage.py makemigrations` before `migrate` since new models are created
* Create a superuser with `python manage.py createsuperuser` to access the admin interface at `/admin/`
* A complete runnable project snapshot is stored in `project_files/`
