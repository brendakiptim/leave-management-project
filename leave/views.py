from django.shortcuts import render
from django.http import HttpResponse
from .models import Leave, Employee


def index(request):
    employees = Employee.objects.all()
    print(employees)
    return render(request,"index.html", {'employees':employees})


