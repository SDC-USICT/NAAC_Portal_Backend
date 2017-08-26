from django.shortcuts import render, redirect
from employee.models import Employee

def school(request):
    if request.method == 'POST' :
        return redirect('employee/index.html',{'error_school':"Error"})
    return render(request, 'employee/index.html', {})


def login(request):
    if request.method == 'GET' :
        return render(request, 'employee/index.html', {})
    dept = request.POST['school']
    school_name = ["usict", "usbt", "usct"]
    if dept not in school_name:
        return render(request,'employee/index.html', {'error_school':"Error"})
    else :
        list = Employee.objects.filter(school=dept)
        return render(request, 'employee/login.html', {
            'dept':dept,
            'list' : list,
        })


def dashboard(request):
    return render(request, 'employee/dashboard.html', {})