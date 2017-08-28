from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def extra(request):
    if request.method == 'GET':
        extraform = ExtraForm()
        print (extraform)
        return render(request,'form.extraform': extraform})
    if request.method == 'POST':
        print (request.POST)
        extraform = ExtraForm(request.POST or None)
        if extraform.is_valid():
            save_it = extraform.save(commit =False)
            save_it.save()
        return HttpResponse('<h1>Your application is saved'</h1>)
