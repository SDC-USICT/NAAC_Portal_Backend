from django.shortcuts import render
from django.http import HttpResponse
from .models import GuestLecturer
from employee.models import Employee
from .forms import GuestLecturerForm

# Create your views here.
def guestlecturer(request):
    if request.method == 'GET':
        guestlecturerform = AwardForm()
        print (awardform)
        return render(request,'form.html', {'guestlecturerform': guestlecturerform})
    if request.method == 'POST':
        print (request.POST)
        guestlecturerform = GuestLecturerForm(request.POST or None)
        if guestlecturerform.is_valid():
            save_it = guestlecturerform.save(commit =False)
            save_it.save()
        return HttpResponse('<h1>Your application is saved'</h1>)
