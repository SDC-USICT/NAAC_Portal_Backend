from django.shortcuts import render
from django.http import HttpResponse
from .models import Membership
from employee.models import Employee
from .forms import MoabForm

# Create your views here.
def moab(request):
    if request.method == 'GET':
        moabform = MoabForm()
        print (moabform)
        return render(request,'form.html', {'moabform': moabform})
    if request.method == 'POST':
        print (request.POST)
        moabform = MoabForm(request.POST or None)
        if moabform.is_valid():
            save_it = moabform.save(commit =False)
            save_it.save()
        return HttpResponse('<h1>Your application is saved</h1>')
