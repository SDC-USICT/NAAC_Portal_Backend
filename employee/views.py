import json

import django
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from employee.models import Employee
from awards.models import Awards
from extra_activities.models import Extra
from guest_lecturer.models import GuestLecturer
from moab.models import Membership
from patents.models import *
from professional_details.models import *
from project.models import *
from publication_details.models import *
from subjects_taken.models import *
from workshop.models import *  # add rebase--continue

@csrf_exempt
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
def columns(request):

    arr = []
    for m in django.apps.apps.get_models():
        arr.append(m.__name__)

    extras =  [
        'LogEntry',
        'Permission',
        'Group',
        'User',
        'ContentType',
        'Session'
       ]

    final = [item for item in arr if item not in extras]

    res = {}

    for modl in final:
        kls = eval(modl)
        res[modl] = []
        for f in kls._meta.get_fields():
            try:
                res[modl].append({
                    'name' : f.name,
                    'verbose' : f.verbose_name
                })
            except Exception:
                res[modl].append({
                    'name': f.name,
                })

    del res['Employee']
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def login(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    password = request['password']

    try:
        a, created = Employee.objects.get(instructor_id=username, password=password)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }

    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def awards(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    title = request['title']
    org = request['organisation']
    month = request['month']
    year = request['year']

    try:
        a, created = Awards.objects.update_or_create(instructor_id=username,title= title, organisation= org, month= month, year= year)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def employee(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    name = request['name']
    email = request['email']
    phone = request['phone']
    designation = request['designation']
    date_join = request['date_of_joining']
    romm = request['room_no']
    school = request['school']
    password = request['password']

    try:
        a, created = Employee.objects.update_or_create(instructor_id=username,name= name, email= email, phone= phone, designation= designation,date_of_joining=date_join,room_no=romm,school=school,password=password)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def extra(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    name = request['name']
    dept = request['department']
    details = request['details']
    year = request['year']

    try:
        a, created = Extra.objects.update_or_create(instructor_id=username,name= name, department= dept, details= details, year= year)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def guest(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    nature = request['nature']
    inst = request['institute']
    date = request['date']
    topic = request['topic']

    try:
        a, created = GuestLecturer.objects.update_or_create(instructor_id=username,nature= nature, institute= inst, date= date, topic= topic)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def moab(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    type = request['type']
    acad_body = request['academic_body']
    univ = request['university_agency']

    try:
        a, created = Membership.objects.update_or_create(instructor_id=username,type= type, academic_body= acad_body, university_agency= univ)
        a.save()
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

    empid_id = request['employee_id']
    academic_experience_id = request['academic_experience']
    industrial_exp_id = request['industrial_exp']
    qualification_before = request['qualification_before']
    qualification_after =  request['qualification_after']
    phds_id = request['phds']
    pursuing_id = request['pursuing']
    submitted_id = request['submitted']
    awarded_id = request['awarded']
    year_id = request['year']

    try:
        a, created = Professional.objects.update_or_create(instructor_id=empid_id,academic_experience= academic_experience_id,
                                                         industrial_exp= industrial_exp_id, qualification_before= qualification_before,
                                                         qualification_after=qualification_after,phds=phds_id,pursuing=pursuing_id,
                                                         submitted=submitted_id,awarded=awarded_id,year= year_id)
        a.save()
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
def workshop(request):
    request = json.loads(request.encode('utf-8'))

    empid_id = request['empid']
    name_id = request['name']
    date_id = request['date']
    duration_id = request['duration']
    organization_id =  request['organization']

    try:
        a, created = Workshop.objects.update_or_create(instructor_id=empid_id,name= name_id,
                                                         date= date_id, duration= duration_id,
                                                         organisation=organization_id)
        a.save()
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
def projects(request):
    request = json.loads(request.encode('utf-8'))

    username = request['empid']
    title_id = request['title']
    pi_id = request['pi']
    copi_id = request['copi']
    sponsors_id = request['sponsors']
    date_of_award_id =  request['date_of_award']
    date_completed_id =  request['date_completed']
    amnt_sanctioned_id =  request['amnt_sanctioned']
    status_id =  request['status']

    try:
        a, created = Projects.objects.update_or_create(instructor_id=username,title=title_id,pi=pi_id,
                                              copi=copi_id,sponsors=sponsors_id,date_of_award=date_of_award_id,
                                              date_completed=date_completed_id,amnt_sanctioned=amnt_sanctioned_id,
                                              status=status_id)
        a.save()
        res = {
            'success' : 'true'
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def patents(request):
    request = json.loads(request.encode('utf-8'))

    username = request['empid']
    name_id = request['name']
    patenting_agency_id = request['patenting_agency']
    year_application_id = request['year_application']
    year_grant_id =  request['year_grant']


    try:
        a, created = Patents.objects.update_or_create(instructor_id=username,name=name_id,patenting_agency=patenting_agency_id,
                                             year_application=year_application_id,year_grant=year_grant_id)
        a.save()
        res = {
            'success' : 'true'
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def subject(request):
    request = json.loads(request.encode('utf-8'))

    name = request['name']
    code = request['code']
    credit = request['credit']


    try:
        a, created = Subject.objects.update_or_create(name=name,code=code,credit=credit)
        a.save()
        res = {
            'success' : 'true'
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def subjectTaken(request):
    request = json.loads(request.encode('utf-8'))

    username = request['empid']
    subjects = request['subjects']
    year = request['year']
    school = request['school']


    try:
        a, created = SubjectsTaken.objects.update_or_create(instructor_id=username,subjects=subjects,year=year,school=school)
        a.save()
        res = {
            'success' : 'true'
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)
