from django.shortcuts import render
from django.http import HttpResponse
from .models import JournalPapers,Conference,BookChapters
from employee.models import Employee
from .forms import PublicationForm


def publication(request):
    if request.method == 'GET':
        publicationform = PublicationForm()
        print(publicationform)
        return render(request, "publication.html", {'publicationform': publicationform})
    if request.method == 'POST':
        print(request.POST)
        publicationform = PublicationForm(request.POST or None)
        if publicationform.is_valid():
            save_it = publicationform.save(commit=False)
            save_it.save()
        return HttpResponse('<h1>Your application is saved</h1> ')
