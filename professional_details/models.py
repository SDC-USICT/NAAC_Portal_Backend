import datetime
from django.db import models

# Create your models here.
from employee.models import Employee


class Professional(models.Model):
    employee = models.ForeignKey(to=Employee, verbose_name='Employee ID')
    title = models.CharField("Academic Experience",max_length=100)
    industrial_exp = models.CharField("Industrial Experience",max_length=100)
    qualification_highest = models.CharField("Highest Qualification",max_length=100)
    qualification_year_completion = models.CharField("Year Of Completion of Highest Qualification",max_length=100)
    phds = models.IntegerField("Total Student")
    pursuing = models.IntegerField("Phd Pursuing")
    submitted = models.IntegerField("Phd Submitted")
    awarded = models.IntegerField("Phd Awarded")
    year = models.CharField("Year",max_length=4, default=(datetime.datetime.now()).year)

    class Meta:
        db_table = 'professional'
