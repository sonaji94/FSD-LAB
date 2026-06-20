from django.shortcuts import render


def fruit_student(request):
    fruitList = ['Mango', 'Kiwi', 'Banana', 'Apple', 'Grapes']
    studentList = ['Rama', 'Chetan', 'Kumar', 'Harish', 'Geetha']

    context = {
        'fruitList': fruitList,
        'studentList': sorted(studentList),
    }
    return render(request, 'listfruit_app/fruits_student.html', context)
