from django.db import models

# Create your models here.
from employee.models import Employee


class Membership(models.Model):
    employee_id = models.ForeignKey(to=Employee, related_name='employee_moab')
    type = models.CharField("Membership Type",max_length=100)
    academic_body = models.CharField("Academic Body Name",max_length=100)
    university_agency = models.CharField("University Agency",max_length=100)

    class Meta:
        db_table = 'membership'
