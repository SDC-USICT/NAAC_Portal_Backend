from django.db import models

# Create your models here.
from employee.models import Employee


class Workshop(models.Model):
    employee = models.ForeignKey(to=Employee, verbose_name='Employee ID')
    title = models.CharField(verbose_name = "Name",max_length=100)
    date = models.TextField(verbose_name = "Date", blank=True, null=True)
    duration = models.IntegerField(verbose_name = "Duration(in days)")
    organization = models.CharField(verbose_name = "Organization",max_length=100)

    class Meta:
        db_table = 'workshop'
