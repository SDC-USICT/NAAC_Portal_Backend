from django.shortcuts import render
from django.http import HttpResponse
from .models import Patents
from employee.models import Employee
from .forms import PatentForm


def patent(request):
    if request.method == 'GET':
        patentsform = PatentForm()
        print(patentsform)
        return render(request, "patent.html", {'patentsform': patentsform})
    if request.method == 'POST':
        print(request.POST)
        patentsform = PatentForm(request.POST or None)
        if patentsform.is_valid():
            save_it = patentsform.save(commit=False)
            save_it.save()
        return HttpResponse('<h1>Your application is saved</h1> ')
