from django.urls import path
from . import views

urlpatterns = [
    path('fruits/', views.fruit_student, name='fruit_student'),
]
