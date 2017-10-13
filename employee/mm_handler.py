# Parser for data from frontend, for classes have many to many foreign key fields.
from django.core.mail import EmailMessage

from naac_portal.settings import FRONTEND
from publication_details.models import Book


def handler(kls, data):
    klass = eval(kls)
    print(data)

    for d in data:
        print(d)
        for sd in d['coauthor'].split(';'):
            if sd.split(':')[2] == '0':
                from employee.models import Employee
                e = Employee.objects.get(instructor_id=d['employee'])
                print('mail ' + sd.split(':')[1])
                stremail = FRONTEND + '/#/approve?id=' + str(d['pk']) + '&title=' + \
                           d['title'] +'&email=' + sd.split(':')[1] + '&type=' +  kls + \
                '&invitee=' + (e.name).replace(' ', '')
                print(stremail)
                mail = EmailMessage('NAAC Portal CoAuthor Verification Mail', stremail, to=[sd.split(':')[1]])
                mail.send()