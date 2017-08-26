from django.shortcuts import render
from django.http import HttpResponse
from .models import Awards
from employee.models import Employee
from .forms import AwardForm

# Create your views here.
def award(request):
    if request.method == 'GET':
        awardform = AwardForm()
        print (awardform)
        return render(request,'form.html', {'awardform': awardform})
    if request.method == 'POST':
        print (request.POST)
        awardform = AwardForm(request.POST or None)
        if awardform.is_valid():
            save_it = awardform.save(commit =False)
            save_it.save()
        return HttpResponse('<h1>Your application is saved'</h1>)
