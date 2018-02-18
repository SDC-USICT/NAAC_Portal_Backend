import copy
import json
import os
import urllib
import traceback
import certifi
import django
from django.core import serializers
from django.core.exceptions import FieldError
from django.core.files.storage import FileSystemStorage
from django.core.mail.backends import console
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.mail import EmailMessage


from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings

from employee.mm_handler import handler
from employee.models import *
from awards.models import Awards
from extra_activities.models import Extra
from guest_lecturer.models import GuestLecture
from moab.models import Membership
from naac_portal import settings
from naac_portal.settings import BASE_DIR
from patents.models import *
from professional_details.models import *
from project.models import *
from publication_details.models import *
from subjects_taken.models import *
from workshop.models import *
from employee.serializer import EmployeeSerializer


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def subs(request):
    subjects = Subject.objects.all()
    final = serializers.serialize('json', subjects)
    return JsonResponse(json.loads(final), safe=False)


@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
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
        'CoAuthors',
        'DontFill'
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


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def login(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    password = request['password']

    try:
        a = Employee.objects.filter(instructor_id=username)
        if a.exists():
            import hashlib

            if hashlib.md5( (str(a[0].password) + str(a[0].salt)).encode('utf-8') ).hexdigest() == password:
                a = a[0]
                serializer = EmployeeSerializer(a)
                token = generate_jwt_token(serializer.data)
                res = {
                    'user': serializer.data,
                    'token': token
                }
                e = Employee.objects.get(instructor_id=username)
                e.salt = None
                e.save()
                return JsonResponse(res, status=201)
            else:
                res = {
                    'error' : 'Password did not match!'
                }
                return JsonResponse(res, status=401)
        else:
            res = {
                'error': 'true'
            }
    except Exception:
        tc = traceback.format_exc()
        print (str(tc))
        res = {
            'error': 'true'
        }

    return JsonResponse(res, safe=False)


@api_view(['POST'])
@authentication_classes((JSONWebTokenAuthentication,))
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


@api_view(['POST'])
@authentication_classes((JSONWebTokenAuthentication,))
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


@api_view(['POST'])
@authentication_classes((JSONWebTokenAuthentication,))
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


@api_view(['POST'])
@authentication_classes((JSONWebTokenAuthentication,))
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


@api_view(['POST'])
@authentication_classes((JSONWebTokenAuthentication,))
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
    role = request['role']
    details = request['detailsworkshop']

    try:
        a, created = Workshop.objects.update_or_create(instructor_id=empid_id, name=name_id,
                                                       date=date_id, duration=duration_id,
                                                       organisation=organization_id,role=role,detailsworkshop=details)
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


@api_view(['POST', 'GET'])
@authentication_classes((JSONWebTokenAuthentication,))
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

    request = json.loads(request.body.decode('utf-8'))
    data = request['data']
    mdata = copy.deepcopy(data)
    kls = request['kls']
    klass = eval(kls)

    coauthor_classes = [
        'Book',
        'BookChapters',
        'JournalPapers',
        'Conference',
        'Projects'
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


@api_view(['POST', 'GET'])
@authentication_classes((JSONWebTokenAuthentication,))
def employee_details(request):
    request = json.loads(request.body.decode('utf-8'))

    empid = request['empid']
    e = Employee.objects.get(instructor_id=empid)
    res = EmployeeSerializer(e)
    return JsonResponse((res.data), safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def update_emp_details(request):
    request = json.loads(request.body.decode('utf-8'))
    request = request['data']
    username = request['instructor_id']
    name = request['name']
    email = request['email']
    phone = request['phone']
    designation = request['designation']
    date_join = request['date_of_joining']
    romm = request['room_no']
    school = request['school']

    try:
        a, created = Employee.objects.update_or_create(instructor_id=username, defaults ={'name':name, 'email' : email, 'phone' : phone,'designation' : designation, 'date_of_joining' : date_join, 'room_no' : romm,'school':school })
        res = EmployeeSerializer(a)
        return JsonResponse((res.data), safe=False, status=200)
    except Exception:
        tc = traceback.format_exc()
        print (tc)
        res = {
            'error': 'true',
            'trace': str(tc)
        }
        return JsonResponse(res, safe=False, status=500)


@api_view(['POST', 'GET'])
@permission_classes((permissions.AllowAny,))
def school_details(request):
    request = json.loads(request.body.decode('utf-8'))
    e = Employee.objects.all()
    res = serializers.serialize('json', e)
    return JsonResponse(json.loads(res), safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def imageUpload(request):
    if request.method == 'POST':
        myfile = request.FILES['image']
        if image_clean(myfile):
            print(image_clean(myfile))
            n = request.POST['name']
            fs = OverwriteStorage(location=BASE_DIR + os.sep + 'static' + os.sep + 'images')
            filename = fs.save(n + '.jpg', myfile)
            uploaded_file_url = fs.url(filename)
            res = {
                'success': 'true',
                'url': '/static' + uploaded_file_url
            }
        else:
            print(image_clean(myfile))
            res = {
                'success': 'false'
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

@csrf_exempt
@require_http_methods(["POST"])
def forgot_password(request):
    request = json.loads(request.body.decode('utf-8'))
    eMail = request["email"]
    empId = request["loginid"]
    emp = Employee.objects.filter(instructor_id=empId)
    if eMail == "" or emp[0].email != eMail:
        res = {"error":'true'}
        return JsonResponse(res, safe=False)
    pwd = "Password for Faculty Data Acquisition System : " + emp[0].password
    email = EmailMessage('Password For FDA System',pwd,to=[eMail])
    try:
        email.send()
    except Exception as e:
        res = {
        "error":'true'
    }
    res = {
        'success': 'true'
    }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def changePassword(request):
    request = json.loads(request.body.decode('utf-8'))
    curpass = request["curpass"]
    newpass = request["newpass"]
    confpass = request["confpass"]
    empId = request["loginid"]
    if newpass == confpass:
        import hashlib
        emp = Employee.objects.get(instructor_id=empId)
        if hashlib.md5(emp.password.encode('utf-8')).hexdigest() == curpass :
            import base64
            print (base64.b64decode(newpass))
            emp.password = base64.b64decode(newpass)
            emp.save()
            res = {
                "success":'true'
            }
        else:
            res = {
                "error":'true'
            }
    else:
        res = {
            "mod":'true'
        }
    return JsonResponse(res, safe=False)


@api_view(['POST', 'GET'])
@authentication_classes((JSONWebTokenAuthentication,))
def getdontfill(request):
    request = json.loads(request.body.decode('utf-8'))
    empid = request['empid']
    print(request)
    e = Employee.objects.get(instructor_id=empid)
    d = DontFill.objects.filter(employee=e)
    res = {}
    if d.exists():
        res = serializers.serialize('json', d)
        res = (json.loads(res))[0]
        print(res)
        del res['model']
        tmp = res['pk']
        res = res['fields']
        res['pk'] = tmp
    else:
        DontFill.objects.create(employee=e)

    return JsonResponse(res, safe=False)


@api_view(['POST'])
@authentication_classes((JSONWebTokenAuthentication,))
def set_dontfill(request):
    print(request.body.decode('utf-8'))
    request = json.loads(request.body.decode('utf-8'))
    pk = request.pop('pk')
    e = Employee.objects.get(instructor_id=pk)
    DontFill.objects.filter(employee=pk).update(**request)
    print(request)
    res = {
    'success' : 'True'
    }

    return JsonResponse(res, safe=False)

def image_clean(image):
    if image.content_type==('image/jpeg' or 'image/png') and image.size<1000000:
        return True
    return False


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def captcha_validator(req, format=None):
    request = json.loads(req.body.decode('utf-8'))
    recaptcha_response = request.pop('captcha')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    data = urllib.parse.urlencode(values).encode()
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req,  cafile=certifi.where())
    result = json.loads(response.read().decode())
    print (result)
    if result['success']:
        return JsonResponse({}, status=200, safe=False)

    else:
        return JsonResponse({}, status=401, safe=False)


@api_view(['POST', 'GET'])
@permission_classes((permissions.AllowAny,))
def get_dh_key(req, format=None):
    request = json.loads(req.body.decode('utf-8'))
    try:
        client_key = request.pop('dh')
        user_id = request.pop('empid')

        sb = 5

        from random import randint
        secret = 13

        server_key =  ( int(client_key) ** secret ) % int(user_id)

        e = Employee.objects.get(instructor_id=user_id)
        e.salt = server_key
        e.save()
        dhkey_client = (int(sb) ** secret) % int(user_id)

        res = {
        'dh_key' : dhkey_client
        }

        e = Employee.objects.get(instructor_id = user_id)
        return JsonResponse(res, safe=False, status=200)
    except:
        tc = traceback.format_exc()
        print (str(tc))
        res = {
        'dh_key' : 'Error!'
        }
        return JsonResponse(res, safe=False, status=500)


def generate_jwt_token(user):
    user_object = Employee.objects.get(pk=user['instructor_id'])
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user_object)
    token = jwt_encode_handler(payload)
    return token
