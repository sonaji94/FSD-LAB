from django.urls import path
from .views import export_books_csv, export_books_pdf

urlpatterns = [
    path('books/export/csv/', export_books_csv, name='export_books_csv'),
    path('books/export/pdf/', export_books_pdf, name='export_books_pdf'),
]
