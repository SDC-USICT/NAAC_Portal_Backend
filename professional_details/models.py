from django.db import models

# Create your models here.
from employee.models import Employee


class Professional(models.Model):
    employee_id = models.ForeignKey(to=Employee)
    academic_experience = models.IntegerField("Academic Experience")
    industrial_exp = models.IntegerField("Industrial Experience")
    qualification_before = models.CharField("Highest Qualification",max_length=100)
    qualification_after = models.CharField("Qualification Added",max_length=100)
    phds = models.CharField("Total Student",max_length=100)
    pursuing = models.CharField("Phd Pursuing",max_length=100)
    submitted = models.CharField("Phd Submitted",max_length=100)
    awarded = models.CharField("Phd Awarded",max_length=100)
    year = models.IntegerField("Year",null=False, blank=False)

    class Meta:
        db_table = 'professional'
