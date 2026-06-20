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
