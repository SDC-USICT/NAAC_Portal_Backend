from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def phdstudentform(request):
    if request.method == 'GET':
        phdstudentform = PhdStudentForm()
        print (phdstudentform)
        return render(request,'form.phdstudentform': phdstudentform})
    if request.method == 'POST':
        print (request.POST)
        phdstudentform = PhdStudentForm(request.POST or None)
        if phdstudentform.is_valid():
            save_it = phdstudentform.save(commit =False)
            save_it.save()
        return HttpResponse('<h1>Your application is saved'</h1>)
