# Experiment-12: Develop a Registration Page for Student Enrolment Without Page Refresh Using AJAX

## Aim

To create a Django application that registers students using an AJAX-based form submission, allowing data to be saved without a full page refresh.

## Prerequisites

* Python 3.x installed
* Django installed
* Visual Studio Code available
* Virtual environment workflow understood from previous experiments
* Basic understanding of jQuery and AJAX

## Folder Contents

```
Experiment-12/
├── README.md
└── project_files/
    └── ajax_registration_project/
        ├── manage.py
        ├── ajax_registration_project/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── registration/
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
                └── register_student.html
```

## Step-by-Step Procedure

### Step 1: Create Django Project

```bash
django-admin startproject ajax_registration_project
```

### Step 2: Navigate into Project Directory and Create App

```bash
cd ajax_registration_project
python manage.py startapp registration
```

### Step 3: Add App to INSTALLED_APPS

In `ajax_registration_project/settings.py`, add:

```python
'registration',
```

### Step 4: Create Student Model

File: `registration/models.py`

```python
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True, default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

### Step 5: Make and Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create StudentForm

File: `registration/forms.py`

```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
```

### Step 7: Create AJAX View

File: `registration/views.py`

```python
from django.shortcuts import render
from django.http import JsonResponse
from .forms import StudentForm

def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})
```

The `student()` view handles both GET (renders the form) and POST (processes via AJAX and returns JSON) requests.

### Step 8: Create Template with AJAX

File: `registration/templates/register_student.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration (AJAX)</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
<div class="container mt-5">
    <h1>Student Registration</h1>
    <div id="response"></div>
    <form id="student-form" method="post">
        {% csrf_token %}
        <div class="form-group">
            <label for="id_first_name">First Name:</label>
            {{ form.first_name }}
        </div>
        <div class="form-group">
            <label for="id_last_name">Last Name:</label>
            {{ form.last_name }}
        </div>
        <div class="form-group">
            <label for="id_email">Email:</label>
            {{ form.email }}
        </div>
        <button type="submit" class="btn btn-primary">Register</button>
    </form>
</div>
<script>
$(document).ready(function() {
    $('#student-form').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/student/',
            data: $(this).serialize(),
            success: function(response) {
                if (response.success) {
                    $('#response').html('<div class="alert alert-success">Student registered successfully.</div>');
                    $('#student-form')[0].reset();
                } else {
                    $('#response').html('<div class="alert alert-danger">Failed to register student.</div>');
                }
            },
            error: function() {
                $('#response').html('<div class="alert alert-danger">Failed to register student.</div>');
            }
        });
    });
});
</script>
</body>
</html>
```

The key AJAX behavior:
* `e.preventDefault()` stops the form from submitting normally
* `$.ajax()` sends a POST request to `/student/` with serialized form data
* On success, a success alert is displayed and the form is reset
* On failure, an error message is shown

### Step 9: Configure URLs

File: `registration/urls.py`

```python
from django.urls import path
from .views import student

urlpatterns = [
    path('student/', student, name='student'),
]
```

File: `ajax_registration_project/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
]
```

### Step 10: Run the Development Server

```bash
python manage.py runserver
```

### Step 11: Open in Browser

Navigate to:

```
http://127.0.0.1:8000/student/
```

## Commands Used

| Step | Command |
|------|---------|
| Create project | `django-admin startproject ajax_registration_project` |
| Enter project | `cd ajax_registration_project` |
| Create app | `python manage.py startapp registration` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Run server | `python manage.py runserver` |

## File Explanations

| File | Purpose |
|------|---------|
| `manage.py` | Django's command-line utility for administrative tasks |
| `ajax_registration_project/settings.py` | Project settings including installed apps, database, templates |
| `ajax_registration_project/urls.py` | Root URL configuration; includes registration app URLs |
| `registration/models.py` | Defines the `Student` model with first_name, last_name, and email |
| `registration/forms.py` | `StudentForm` ModelForm with Bootstrap widget styling |
| `registration/views.py` | `student()` view handling GET (form display) and POST (AJAX JSON response) |
| `registration/urls.py` | App-level URL routing mapping `/student/` to the view |
| `registration/templates/register_student.html` | Form template with jQuery AJAX for page-refresh-free submission |

## Expected Output

After running `python manage.py runserver` and visiting `http://127.0.0.1:8000/student/`:

* A student registration form appears with First Name, Last Name, and Email fields
* Filling in the fields and clicking "Register" submits the data via AJAX
* The page does NOT refresh during submission
* A green success alert "Student registered successfully." appears
* The form clears automatically after successful submission
* If validation fails, a red error alert appears
* The student record is saved in the database

## Conclusion

This experiment demonstrates how to implement AJAX-based form submission in Django. Instead of the traditional synchronous POST (which causes a page refresh), the form data is sent asynchronously using jQuery's `$.ajax()` method. The Django view detects the POST request, validates and saves the data, and returns a JSON response. The client-side JavaScript handles the response to show success or error messages without reloading the page. This technique is fundamental for building modern, responsive web applications.

## Notes

* Activate the virtual environment before running Django commands
* Run `python manage.py makemigrations` before `migrate` since new models are created
* jQuery and Bootstrap are loaded from CDN, so an internet connection is required
* The `{% csrf_token %}` is included in the form; jQuery's `serialize()` includes it automatically
* A complete runnable project snapshot is stored in `project_files/`
