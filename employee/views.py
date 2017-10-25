import copy
import json
import os

import django
from django.core import serializers
from django.core.exceptions import FieldError
from django.core.files.storage import FileSystemStorage
from django.core.mail.backends import console
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from employee.mm_handler import handler
from employee.models import Employee
from awards.models import Awards
from extra_activities.models import Extra
from guest_lecturer.models import GuestLecture
from moab.models import Membership
from naac_portal.settings import BASE_DIR
from patents.models import *
from professional_details.models import *
from project.models import *
from publication_details.models import *
from subjects_taken.models import *
from workshop.models import *  # add rebase--continue


# TODO: ADD VALIDATOR FOR CHECKING IF kls FROM FRONTEND
# TODO: IS A PART OF ALREADY EXISTENT MODELS IN BACKEND

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

    extras = [
        'LogEntry',
        'Permission',
        'Group',
        'User',
        'ContentType',
        'Session',
        'Subject',
        'CoAuthors'
    ]

    final = [item for item in arr if item not in extras]

    res = {}

    for modl in final:
        kls = eval(modl)
        res[modl] = []
        for f in kls._meta.get_fields():
            try:
                res[modl].append({
                    'name': f.name,
                    'verbose': f.verbose_name
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
        a = Employee.objects.filter(instructor_id=username, password=password)
        if a.exists():
            res = {
                'success': 'true',
            }
        else:
            res = {
                'error': 'true'
            }
    except Exception:
        res = {
            'error': 'true'
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
        a, created = Awards.objects.update_or_create(instructor_id=username, title=title, organisation=org, month=month,
                                                     year=year)
        a.save()
        res = {
            'success': 'true',
        }
    except Exception:
        res = {
            'error': 'true'
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
        a, created = Employee.objects.update_or_create(instructor_id=username, name=name, email=email, phone=phone,
                                                       designation=designation, date_of_joining=date_join, room_no=romm,
                                                       school=school, password=password)
        a.save()
        res = {
            'success': 'true',
        }
    except Exception:
        res = {
            'error': 'true'
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
        a, created = Extra.objects.update_or_create(instructor_id=username, name=name, department=dept, details=details,
                                                    year=year)
        a.save()
        res = {
            'success': 'true',
        }
    except Exception:
        res = {
            'error': 'true'
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
        a, created = GuestLecture.objects.update_or_create(instructor_id=username, nature=nature, institute=inst,
                                                           date=date, topic=topic)
        a.save()
        res = {
            'success': 'true',
        }
    except Exception:
        res = {
            'error': 'true'
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
        a, created = Membership.objects.update_or_create(instructor_id=username, type=type, academic_body=acad_body,
                                                         university_agency=univ)
        a.save()
        res = {
            'success': 'true',
        }
    except Exception:
        res = {
            'error': 'true'
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
    qualification_after = request['qualification_after']
    phds_id = request['phds']
    pursuing_id = request['pursuing']
    submitted_id = request['submitted']
    awarded_id = request['awarded']
    year_id = request['year']

    try:
        a, created = Professional.objects.update_or_create(instructor_id=empid_id,
                                                           academic_experience=academic_experience_id,
                                                           industrial_exp=industrial_exp_id,
                                                           qualification_before=qualification_before,
                                                           qualification_after=qualification_after, phds=phds_id,
                                                           pursuing=pursuing_id,
                                                           submitted=submitted_id, awarded=awarded_id, year=year_id)
        a.save()
        res = {
            'success': 'true',
        }
    except Exception:
        res = {
            'error': 'true'
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
    organization_id = request['organization']

    try:
        a, created = Workshop.objects.update_or_create(instructor_id=empid_id, name=name_id,
                                                       date=date_id, duration=duration_id,
                                                       organisation=organization_id)
        a.save()
        res = {
            'success': 'true',
        }
    except Exception:
        res = {
            'error': 'true'
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
    date_of_award_id = request['date_of_award']
    date_completed_id = request['date_completed']
    amnt_sanctioned_id = request['amnt_sanctioned']
    status_id = request['status']

    try:
        a, created = Projects.objects.update_or_create(instructor_id=username, title=title_id, pi=pi_id,
                                                       copi=copi_id, sponsors=sponsors_id,
                                                       date_of_award=date_of_award_id,
                                                       date_completed=date_completed_id,
                                                       amnt_sanctioned=amnt_sanctioned_id,
                                                       status=status_id)
        a.save()
        res = {
            'success': 'true'
        }
    except Exception:
        res = {
            'error': 'true'
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
    year_grant_id = request['year_grant']

    try:
        a, created = Patents.objects.update_or_create(instructor_id=username, name=name_id,
                                                      patenting_agency=patenting_agency_id,
                                                      year_application=year_application_id, year_grant=year_grant_id)
        a.save()
        res = {
            'success': 'true'
        }
    except Exception:
        res = {
            'error': 'true'
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
        a, created = Subject.objects.update_or_create(name=name, code=code, credit=credit)
        a.save()
        res = {
            'success': 'true'
        }
    except Exception:
        res = {
            'error': 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def subjectTaken(request):
    request = json.loads(request.body.decode('utf-8'))

    username = request['empid']
    subjects = request['subjects']
    year = request['year']
    school = request['school']

    try:
        a, created = SubjectsTaken.objects.update_or_create(instructor_id=username, subjects=subjects, year=year,
                                                            school=school)
        a.save()
        res = {
            'success': 'true'
        }
    except Exception:
        res = {
            'error': 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def get_data(request):
    request = json.loads(request.body.decode('utf-8'))

    empid = request['empid']
    kls = request['kls']

    arr = []
    for m in django.apps.apps.get_models():
        arr.append(m.__name__)

    if kls in arr:
        klass = eval(kls)
        e = Employee.objects.get(instructor_id=empid)
        result = klass.objects.filter(employee=e)
        res = serializers.serialize('json', result)
        i = 0
        res = json.loads(res)
        for f in res:
            tmp = res[i]['pk']
            res[i] = res[i]['fields']
            res[i]['pk'] = tmp
            i = i + 1
    else:
        print('Invalid Request!')
        res = {
            'error': "Invalid!"
        }

    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def post_data(request):
    myfile = request.FILES.get('image')
    print(request.FILES)

    print(myfile)
    request = json.loads(request.body.decode('utf-8'))
    print(request)
    data = request['data']
    print(data)
    mdata = copy.deepcopy(data)
    kls = request['kls']
    klass = eval(kls)

    coauthor_classes = [
        'Book',
        'BookChapters',
        'JournalPapers',
        'Conference'
    ]

    d = data[0]

    if kls == 'SubjectsTaken' :
        try:
            d.pop('image')
        except KeyError:
            print('No Image!')

    try:
        pk = d.pop('pk')
        try:
            d.pop('$$hashKey')
        except KeyError:
            print('Hash not found!')
        empid = d.pop('employee')  # New element, therefore no pk assigned yet
        if not pk:
            e = Employee.objects.get(instructor_id=empid)
            k = klass.objects.create(employee=e, **d)
            k.save()

        # Old element, just update its data
        else:
            k = klass.objects.filter(id=pk)
            if k.exists():
                klass.objects.filter(id=pk).update(**d)
            else:
                res = {
                    'error': 'Employee ID does not exist'
                }
                return JsonResponse(res, safe=False)

    except KeyError:

        empid = d.pop('employee')
        e = Employee.objects.get(instructor_id=empid)
        k = klass.objects.create(employee=e, **d)
        k.save()


    res = {
        'success': 'true'
    }
    klass = eval(kls)
    e = Employee.objects.get(instructor_id=empid)

    if type(k) != django.db.models.query.QuerySet and kls in coauthor_classes:

        result = klass.objects.filter(employee=e, pk=k.pk)
        final1 = serializers.serialize('json', result)

        i = 0

        final1 = json.loads(final1)
        for f in final1:
            tmp = final1[i]['pk']
            final1[i] = final1[i]['fields']
            final1[i]['pk'] = tmp
            i = i + 1


        handler(kls, final1)

    klass = eval(kls)
    e = Employee.objects.get(instructor_id=empid)
    result = klass.objects.filter(employee=e)
    final = serializers.serialize('json', result)

    i = 0

    final = json.loads(final)
    for f in final:
        tmp = final[i]['pk']
        final[i] = final[i]['fields']
        final[i]['pk'] = tmp
        i = i + 1


    res['data'] = final
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def delete_data(request):
    request = json.loads(request.body.decode('utf-8'))
    data = request['data']
    kls = request['kls']
    empid = request['empid']
    klass = eval(kls)
    pk = data.pop('pk')

    try:
        entry = klass.objects.get(id=pk)
        entry.delete()

    except Exception:
        res = {
            'error': 'true'

        }

        return JsonResponse(res, safe=False)

    res = {
        'success': 'true'
    }

    klass = eval(kls)
    e = Employee.objects.get(instructor_id=empid)
    result = klass.objects.filter(employee=e)
    final = serializers.serialize('json', result)
    i = 0

    final = json.loads(final)
    for f in final:
        tmp = final[i]['pk']
        final[i] = final[i]['fields']
        final[i]['pk'] = tmp
        i = i + 1
    res['data'] = final
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def employee_details(request):
    request = json.loads(request.body.decode('utf-8'))

    empid = request['empid']
    e = Employee.objects.get(instructor_id=empid)
    res = serializers.serialize('json', [e])
    return JsonResponse(json.loads(res), safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def update_emp_details(request):
    request = json.loads(request.body.decode('utf-8'))
    data = request['data']
    pk = data.pop('pk')
    Employee.objects.filter(instructor_id=pk).update(**data)
    e = Employee.objects.get(instructor_id=pk)
    res = serializers.serialize('json', [e])
    return JsonResponse(json.loads(res), safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def school_details(request):
    request = json.loads(request.body.decode('utf-8'))
    school = request['school']
    e = Employee.objects.filter(school=school)
    res = serializers.serialize('json', e)
    return JsonResponse(json.loads(res), safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def imageUpload(request):
    if request.method == 'POST':
        myfile = request.FILES['image']
        n = request.POST['name']
        fs = OverwriteStorage(location=BASE_DIR + os.sep + 'static' + os.sep + 'images')
        filename = fs.save(n + '.jpg', myfile)
        uploaded_file_url = fs.url(filename)
        res = {
            'success': 'true',
            'url': '/static' + uploaded_file_url
        }
    else:
        res = {
            'success': 'false'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def subjectImageUpload(request):
    if request.method == 'POST':
        myfile = request.FILES['image']
        n = request.POST['name']
        p = request.POST['filename']
        try:
            os.mkdir(BASE_DIR + os.sep + 'static' + os.sep + 'images' + os.sep + n)
            os.mkdir(BASE_DIR + os.sep + 'static' + os.sep + 'images' + os.sep + n + os.sep + 'subjects')

        except OSError as e:
            if e.errno == 17:
                pass

        fs = OverwriteStorage(location=BASE_DIR + os.sep + 'static' + os.sep + 'images' + os.sep + n + os.sep + 'subjects')
        filename = fs.save(p + '.jpg', myfile)
        uploaded_file_url = fs.url(filename)
        res = {
            'success': 'true',
            'url': '/static' + uploaded_file_url
        }
    else:
        res = {
            'success': 'false'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def verify_coauthor(request):
    request = json.loads(request.body.decode('utf-8'))

    kls = request['type']
    email = request['email']
    klass = eval(kls)
    pk = request['pk']
    status = request['status']
    c = klass.objects.get(id=pk)
    tmp = []
    tmp2 = []
    for cs in c.coauthor.split(';'):
        if cs.split(':')[1] == email and status == '1':
            cs = cs.split(':')
            cs[2] = '1'

            o = Employee.objects.filter(email=email)
            if o.exists():
                o = o[0]
                cs[0] = o.name

            cs = ':'.join(cs)
            tmp.append(cs)

        elif status == '0':
            pass
        else:
            tmp2.append(cs)
            tmp.append(cs)

    tmp = ';'.join(tmp)
    c.coauthor = tmp
    c.save()

    tmp2 = ';'.join(tmp2)
    if status == '1':
        e = Employee.objects.filter(email=email)
        if e.exists():
            e = e[0]
            extra = klass.objects.get(id=pk)
            extra.pk = None
            extra.employee = e
            extra.author = e.name
            extra.coauthor = tmp2 + ';' + c.employee.name + ':' + c.employee.email + ':1'
            extra.save()

    res = {
        'success': 'true'
    }

    return JsonResponse(res, safe=False)


class OverwriteStorage(FileSystemStorage):
    def _save(self, name, content):
        self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name, max_length=None):
        return name
