# Parser for data from frontend, for classes have many to many foreign key fields.
from django.core.mail import EmailMessage

from naac_portal.settings import FRONTEND
from publication_details.models import *
from project.models import *


def handler(kls, data):
    klass = eval(kls)

    copi_flag = False
    if kls == 'Projects':
        spec = 'Co Principle Investigator'
        copi_flag = True
    else:
        spec = 'Co Author'
    for d in data:

        if d['coauthor']:
            for sd in d['coauthor'].split(';'):
                if sd.split(':')[2] == '0':
                    from employee.models import Employee
                    e = Employee.objects.get(instructor_id=d['employee'])
                    search = Employee.objects.filter(email=sd.split(':')[1])
                    print(sd.split(':')[1])
                    if search.exists():
                        stremail = FRONTEND + '/#/approve?id=' + str(d['pk']) + '&title=' + \
                                   d['title'] +'&email=' + sd.split(':')[1] + '&type=' +  kls + \
                        '&invitee=' + (e.name).replace(' ', '') + '&copi=' + str(copi_flag)


                        mail = EmailMessage('NAAC Portal ' + spec +' Verification Mail', stremail, to=[sd.split(':')[1]])
                        try:
                            mail.send()
                        except Exception:
                            print('Mail Fault')
                    else:
                        print('Employee not exists in table')