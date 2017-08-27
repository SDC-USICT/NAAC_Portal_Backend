from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from employee.models import Employee


@require_http_methods(["GET", "POST"])
def schools(request):
    schools = [
        'usict',
        'uslls',
        'usct'
    ]

    return JsonResponse(schools, safe=False)