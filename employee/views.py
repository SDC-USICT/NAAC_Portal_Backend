import json

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from employee.models import Employee
from professional_details.models import Professional
from workshop.models import Workshop
from project.models import Projects
from patents.models import Patents


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

@csrf_exempt
@require_http_methods(["POST"])
def professional(request):
    request = json.loads(request.encode('utf-8'))

    empid_id = request['empid']
    academic_experience_id = request['academic_experience']
    industrial_exp_id = request['industrial_exp']
    qualification_before = request['qualification_before']
    qualification_after =  request['qualification_after']
    phds_id = request['phds']
    pursuing_id = request['pursuing']
    submitted_id = request['submitted']
    awarded_id = request['awarded']
    year_id = request['year']

    e= Employee.objects.get(instructor_id=empid_id)
    res={

    }

    a = Professional.objects.update_or_create(employee_id=e)
    try:
        a.save()
        res['success'] ='true'
    except Exception:
        res['error'] = 'true'
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def workshop(request):
    request = json.loads(request.encode('utf-8'))

    empid_id = request['empid']
    name_id = request['name']
    date_id = request['date']
    duration_id = request['duration']
    organization_id =  request['organization']


    e= Employee.objects.get(instructor_id=empid_id)
    res={

    }

    a = Workshop.objects.update_or_create(employee_id=e)
    try:
        a.save()
        res['success'] ='true'
    except Exception:
        res['error'] = 'true'
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def projects(request):
    request = json.loads(request.encode('utf-8'))

    title_id = request['title']
    pi_id = request['pi']
    copi_id = request['copi']
    sponsors_id = request['sponsors']
    date_of_award_id =  request['date_of_award']
    date_completed_id =  request['date_completed']
    amnt_sanctioned_id =  request['amnt_sanctioned']
    status_id =  request['status']


    e= Employee.objects.get(instructor_id=empid_id)
    res={

    }

    a = Projects.objects.update_or_create(employee_id=e)
    try:
        a.save()
        res['success'] ='true'
    except Exception:
        res['error'] = 'true'
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def patents(request):
    request = json.loads(request.encode('utf-8'))

    name_id = request['name']
    patenting_agency_id = request['patenting_agency']
    year_application_id = request['year_application']
    year_grant_id =  request['year_grant']


    e= Employee.objects.get(instructor_id=empid_id)
    res={

    }
    a = Patents.objects.update_or_create(employee_id=e)
    try:
        a.save()
        res['success'] ='true'
    except Exception:
        res['error'] = 'true'
    return JsonResponse(res, safe=False)
