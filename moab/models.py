from django.db import models

# Create your models here.
from employee.models import Employee


class Membership(models.Model):
    employee_id = models.ForeignKey(to=Employee, related_name='employee_moab')
    type = models.CharField(max_length=100)
    academic_body = models.CharField(max_length=100)
    university_agency = models.CharField(max_length=100)

    class Meta:
        db_table = 'membership'
