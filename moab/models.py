from django.db import models

# Create your models here.
from employee.models import Employee


class Membership(models.Model):
    employee = models.ForeignKey(to=Employee, related_name='employee_moab', verbose_name='Employee ID', on_delete=models.PROTECT)
    title= models.CharField("Academic Body Name",max_length=100)
    membership_no= models.IntegerField("Membership Type")
    type = models.CharField("Membership Type",max_length=100)
    start_year = models.CharField("Start Year", max_length=4)
    end_year = models.CharField("End Year", max_length=4,default=2099)


    class Meta:
        db_table = 'membership'
