from django.db import models

# Create your models here.
from employee.models import Employee


class Professional(models.Model):
    employee = models.ForeignKey(to=Employee, verbose_name='Employee ID')
    title = models.IntegerField("Academic Experience")
    industrial_exp = models.IntegerField("Industrial Experience")
    qualification_before = models.CharField("Highest Qualification",max_length=100)
    qualification_after = models.CharField("Qualification Added",max_length=100)
    phds = models.IntegerField("Total Student")
    pursuing = models.CharField("Phd Pursuing",max_length=100)
    submitted = models.IntegerField("Phd Submitted")
    awarded = models.CharField("Phd Awarded",max_length=100)
    year = models.CharField("Year",max_length=4)

    class Meta:
        db_table = 'professional'
