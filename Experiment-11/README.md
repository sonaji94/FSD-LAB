# Experiment-11: Develop a Django App That Performs CSV and PDF Generation for Models

## Aim

To create a Django application that generates CSV and PDF reports from model data using Python's built-in `csv` module and the `xhtml2pdf` library, with a Book model as an example.

## Prerequisites

* Python 3.x installed
* Django installed
* `xhtml2pdf` library installed (`pip install xhtml2pdf`)
* Visual Studio Code available
* Virtual environment workflow understood from previous experiments

## Folder Contents

```
Experiment-11/
├── README.md
└── project_files/
    └── fullstack_project/
        ├── manage.py
        ├── create_book_data.py
        ├── fullstack_project/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── books/
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
                └── books/
                    └── book_list.html
```

## Step-by-Step Procedure

### Step 1: Create Django Project

```bash
django-admin startproject fullstack_project
```

### Step 2: Navigate into Project Directory and Create App

```bash
cd fullstack_project
python manage.py startapp books
```

### Step 3: Add App to INSTALLED_APPS

In `fullstack_project/settings.py`, add:

```python
'books',
```

### Step 4: Create Models

File: `books/models.py`

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
```

### Step 5: Make and Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Views for CSV and PDF Export

File: `books/views.py`

```python
import csv

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import Book


def export_books_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Author', 'Publication Date'])

    books = Book.objects.all().values_list('title', 'author', 'publication_date')
    for book in books:
        writer.writerow(book)

    return response


def export_books_pdf(request):
    books = Book.objects.all()
    template_path = 'books/book_list.html'
    context = {'books': books}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="books.pdf"'

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
```

### Step 7: Create Template for PDF

File: `books/templates/books/book_list.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Book List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <h1>Book List</h1>
    <table>
        <thead>
            <tr>
                <th>Title</th>
                <th>Author</th>
                <th>Publication Date</th>
            </tr>
        </thead>
        <tbody>
            {% for book in books %}
            <tr>
                <td>{{ book.title }}</td>
                <td>{{ book.author }}</td>
                <td>{{ book.publication_date }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

### Step 8: Configure URLs

File: `books/urls.py`

```python
from django.urls import path
from .views import export_books_csv, export_books_pdf

urlpatterns = [
    path('books/export/csv/', export_books_csv, name='export_books_csv'),
    path('books/export/pdf/', export_books_pdf, name='export_books_pdf'),
]
```

File: `fullstack_project/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
]
```

### Step 9: Create Sample Book Data

File: `create_book_data.py`

```python
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fullstack_project.settings')

import django
django.setup()

from books.models import Book

Book.objects.bulk_create([
    Book(title='To Kill a Mockingbird', author='Harper Lee', publication_date='1960-07-11'),
    Book(title='1984', author='George Orwell', publication_date='1949-06-08'),
    Book(title='Pride and Prejudice', author='Jane Austen', publication_date='1813-01-28'),
    Book(title='The Great Gatsby', author='F. Scott Fitzgerald', publication_date='1925-04-10'),
    Book(title='The Catcher in the Rye', author='J.D. Salinger', publication_date='1951-07-16'),
])

print("Book data created successfully.")
```

Run the script:

```bash
python create_book_data.py
```

### Step 10: Install xhtml2pdf

```bash
pip install xhtml2pdf
```

### Step 11: Run the Development Server

```bash
python manage.py runserver
```

### Step 12: Open in Browser

Navigate to:

* `http://127.0.0.1:8000/books/export/csv/` — downloads a CSV file with book data
* `http://127.0.0.1:8000/books/export/pdf/` — downloads a PDF file with book data rendered using the HTML template

## Commands Used

| Step | Command |
|------|---------|
| Create project | `django-admin startproject fullstack_project` |
| Enter project | `cd fullstack_project` |
| Create app | `python manage.py startapp books` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Install xhtml2pdf | `pip install xhtml2pdf` |
| Create sample data | `python create_book_data.py` |
| Run server | `python manage.py runserver` |

## File Explanations

| File | Purpose |
|------|---------|
| `manage.py` | Django's command-line utility for administrative tasks |
| `fullstack_project/settings.py` | Project settings including installed apps, database, templates |
| `fullstack_project/urls.py` | Root URL configuration; includes app URLs and admin |
| `books/models.py` | Defines the `Book` model with title, author, and publication_date |
| `books/views.py` | Contains `export_books_csv` and `export_books_pdf` views for file generation |
| `books/urls.py` | App-level URL routing for CSV and PDF export endpoints |
| `books/admin.py` | Registers Book model in Django admin |
| `books/templates/books/book_list.html` | HTML template styled for PDF rendering via xhtml2pdf |
| `create_book_data.py` | Standalone script to populate the database with sample book records |

## Expected Output

* `http://127.0.0.1:8000/books/export/csv/` — triggers download of `books.csv` containing all book records with columns Title, Author, and Publication Date
* `http://127.0.0.1:8000/books/export/pdf/` — triggers download of `books.pdf` containing a styled table of all book records

## Conclusion

This experiment demonstrates how to generate CSV and PDF files from Django model data. CSV generation uses Python's built-in `csv` module to write tabular data as a downloadable response. PDF generation uses the `xhtml2pdf` library to convert an HTML template with CSS styling into a PDF document. The same approach can be applied to any Django model for generating reports, invoices, or data exports.

## Notes

* Install `xhtml2pdf` using `pip install xhtml2pdf` before running the PDF export
* Run `python create_book_data.py` to populate sample data before testing the exports
* Activate the virtual environment before running Django commands
* A complete runnable project snapshot is stored in `project_files/`
