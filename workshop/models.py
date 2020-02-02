from django.db import models

# Create your models here.
from employee.models import Employee


class Workshop(models.Model):
    employee = models.ForeignKey(to=Employee, verbose_name='Employee ID', on_delete=models.PROTECT)
    title = models.CharField(verbose_name = "Name",max_length=100)
    role = models.CharField(verbose_name = "Role",max_length=100)
    date = models.TextField(verbose_name = "Date", blank=True, null=True)
    duration = models.CharField(verbose_name = "Duration(in days)",max_length=100)
    organization = models.CharField(verbose_name = "Organization",max_length=100)
    detailsworkshop = models.CharField(max_length=100,blank=True,null=True)
    class Meta:
        db_table = 'workshop'
