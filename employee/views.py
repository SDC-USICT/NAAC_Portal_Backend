import json

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from employee.models import Employee


@require_http_methods(["GET", "POST"])
def schools(request):
    schools = [
        'usict',
        'uslls',
        'usct',
        'usbt'
    ]

    return JsonResponse(schools, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def login(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    password = request['password']

    res = {}
    try:
        e = Employee.objects.get(instructor_id=username, password=password)
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }

    return JsonResponse(res, safe=False)

