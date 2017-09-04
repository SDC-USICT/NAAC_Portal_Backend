from django.db import models

# Create your models here.
from employee.models import Employee


class Extra(models.Model):
    employee = models.ForeignKey(to=Employee, verbose_name='Employee ID')
    title = models.CharField("Name",max_length=100)
    department = models.CharField("Department",max_length=100)
    details = models.CharField("Details",max_length=100)
    year = models.IntegerField("Year")


    class Meta:
        db_table = 'extras'
