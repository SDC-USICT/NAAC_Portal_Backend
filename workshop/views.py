from django.shortcuts import render
from django.http import HttpResponse
from .models import Workshop
from employee.models import Employee
from .forms import WorkshopForm


def workshop(request):
    if request.method == 'GET':
        workshopform = WorkshopForm()
        print(workshopform)
        return render(request, "patent.html", {'workshopform': workshopform})
    if request.method == 'POST':
        print(request.POST)
        workshopform = WorkshopForm(request.POST or None)
        if workshopform.is_valid():
            save_it = workshopform.save(commit=False)
            save_it.save()
        return HttpResponse('<h1>Your application is saved</h1> ')
