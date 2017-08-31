from django.db import models

# Create your models here.
from employee.models import Employee


class Workshop(models.Model):
    employee_id = models.ForeignKey(to=Employee, verbose_name='Employee ID')
    name = models.CharField(verbose_name = "Name",max_length=100)
    date = models.DateField(verbose_name = "Date")
    duration = models.CharField(verbose_name = "Duration(in days)",max_length=100)
    organization = models.CharField(verbose_name = "Organization",max_length=100)

    class Meta:
        db_table = 'workshop'
