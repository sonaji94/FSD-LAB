# Experiment-10: Create Generic Class Views for Student List and Student Detail

## Aim

To create generic class-based views (`ListView` and `DetailView`) for the Student model in the student enrolment application, displaying a list of students and detailed information for a selected student.

## Prerequisites

* Python 3.x installed
* Django installed
* Visual Studio Code available
* Virtual environment workflow understood from previous experiments
* Understanding of Django models, forms, and function-based views from Experiments 07-09

## Folder Contents

```
Experiment-10/
├── README.md
└── project_files/
    └── student_generic_view_project/
        ├── manage.py
        ├── student_generic_view_project/
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
                    ├── student_list.html
                    ├── stu_list.html
                    └── student_detail.html
```

## Step-by-Step Procedure

### Step 1: Create Django Project

```bash
django-admin startproject student_generic_view_project
```

### Step 2: Navigate into Project Directory and Create App

```bash
cd student_generic_view_project
python manage.py startapp student_course_registration_app
```

### Step 3: Add App to INSTALLED_APPS

In `student_generic_view_project/settings.py`, add:

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

### Step 6: Create Generic Class-Based Views

File: `student_course_registration_app/views.py`

```python
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Course, Student, Project
from .forms import StudentForm, CourseForm, ProjectForm

def index(request):
    courses = Course.objects.all()
    projects = Project.objects.all()
    students = Student.objects.all()
    return render(request, 'registration/index.html', {
        'courses': courses,
        'projects': projects,
        'students': students,
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

class StudentListView(ListView):
    model = Student
    template_name = 'registration/stu_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'registration/student_detail.html'
    context_object_name = 'student'
```

The `StudentListView` extends Django's generic `ListView` and renders all students using the `stu_list.html` template. The `StudentDetailView` extends `DetailView` and shows individual student details in `student_detail.html`.

### Step 7: Add URL Patterns

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
    path('students/', views.StudentListView.as_view(), name='student_list_all'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
]
```

File: `student_generic_view_project/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_course_registration_app.urls')),
]
```

### Step 8: Create Templates

#### `templates/registration/stu_list.html`

```html
{% extends 'base.html' %}
{% block content %}
<h1>Students</h1>
<ul>
    {% for student in students %}
        <li>
            <a href="{% url 'student_detail' student.pk %}">
                {{ student.first_name }} {{ student.last_name }}
            </a>
        </li>
    {% endfor %}
</ul>
{% endblock %}
```

#### `templates/registration/student_detail.html`

```html
{% extends 'base.html' %}
{% block content %}
<div class="container my-5">
    <div class="row">
        <div class="col-md-6 offset-md-3">
            <div class="card">
                <div class="card-body">
                    <h1 class="card-title">Name: {{ student.first_name }} {{ student.last_name }}</h1>
                    <h1 class="card-title">Email: {{ student.email }}</h1>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

The `index.html` template is updated to also display a students section with links to the detail page:

```html
<h1 class="mt-5 my-5">Students</h1>
<ul class="list-group mt-3">
    {% for student in students %}
        <li class="list-group-item">
            <a href="{% url 'student_detail' student.pk %}">
                {{ student.first_name }} {{ student.last_name }}
            </a>
        </li>
    {% endfor %}
</ul>
```

### Step 9: Make Migrations

```bash
python manage.py makemigrations
```

### Step 10: Apply Migrations

```bash
python manage.py migrate
```

### Step 11: Run the Development Server

```bash
python manage.py runserver
```

### Step 12: Open in Browser

Navigate to:

* `http://127.0.0.1:8000/index/` — main page with courses, projects, and students
* `http://127.0.0.1:8000/students/` — generic list view of all students
* `http://127.0.0.1:8000/students/1/` — detail view for a specific student

## Commands Used

| Step | Command |
|------|---------|
| Create project | `django-admin startproject student_generic_view_project` |
| Enter project | `cd student_generic_view_project` |
| Create app | `python manage.py startapp student_course_registration_app` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Run server | `python manage.py runserver` |

## File Explanations

| File | Purpose |
|------|---------|
| `manage.py` | Django's command-line utility for administrative tasks |
| `student_generic_view_project/settings.py` | Project settings including installed apps, database, templates |
| `student_generic_view_project/urls.py` | Root URL configuration; includes app URLs and admin |
| `student_course_registration_app/models.py` | Defines `Course`, `Project`, and `Student` models |
| `student_course_registration_app/forms.py` | Model forms for `Student`, `Course`, and `Project` |
| `student_course_registration_app/views.py` | Contains function-based views and generic class-based `StudentListView` and `StudentDetailView` |
| `student_course_registration_app/urls.py` | App-level URL routing including `students/` and `students/<int:pk>/` |
| `templates/registration/stu_list.html` | Template for the generic student list view |
| `templates/registration/student_detail.html` | Template for the generic student detail view |

## Expected Output

After running `python manage.py runserver`:

* `http://127.0.0.1:8000/index/` shows a list of courses (clickable to view registered students), a projects list, and a students list with links to student detail pages
* `http://127.0.0.1:8000/students/` shows a clean list of all students with links to their detail pages
* `http://127.0.0.1:8000/students/<pk>/` shows a student detail card with name and email
* The register student/course/project forms work as in previous experiments

## Conclusion

This experiment demonstrates Django's generic class-based views — `ListView` and `DetailView` — to display model data with minimal code. Instead of writing function-based views with manual querysets and template context, the class-based views automatically handle common patterns. The experiment shows how to integrate generic views alongside existing function-based views in the same application, providing both the traditional enrolment functionality and the new list/detail navigation for students.

## Notes

* Activate the virtual environment before running Django commands
* Run `python manage.py makemigrations` before `migrate` since new models are created
* Create a superuser with `python manage.py createsuperuser` to access the admin interface at `/admin/`
* The generic views use `context_object_name` to control the template variable name
* A complete runnable project snapshot is stored in `project_files/`
