from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################
def student_list_complete(request):

    posts = Student.objects.all()
    print("Informaicon de la Consulta: ")
    print(posts)
    
    print("Queries: ")
    print(posts.query)
    
    print("Connection queries: ")
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})


def student_list_filter(request):
    posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')
    
    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})


def student_list(request):
    posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q (surname__startswith='baldwin') | Q (surname__startswith='avery-parker'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})