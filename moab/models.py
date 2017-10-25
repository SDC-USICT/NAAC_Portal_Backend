from django.db import models

# Create your models here.
from employee.models import Employee


class Membership(models.Model):
    employee = models.ForeignKey(to=Employee, related_name='employee_moab', verbose_name='Employee ID')
    title = models.CharField("Membership Type",max_length=100)
    academic_body = models.CharField("Academic Body Name",max_length=100)
    university_agency = models.CharField("University Agency",max_length=100)
    start_year = models.CharField("Start Year", max_length=4)
    end_year = models.CharField("End Year", max_length=4)


    class Meta:
        db_table = 'membership'
