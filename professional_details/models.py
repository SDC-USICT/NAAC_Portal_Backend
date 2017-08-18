from django.db import models

# Create your models here.
from employee.models import Employee


class Professional(models.Model):
    employee_id = models.ForeignKey(to=Employee)
    academic_experience = models.IntegerField()
    industrial_exp = models.IntegerField()
    qualification_before = models.CharField(max_length=100)
    qualification_after = models.CharField(max_length=100)
    phds = models.CharField(max_length=100)
    pursuing = models.CharField(max_length=100)
    submitted = models.CharField(max_length=100)
    awarded = models.CharField(max_length=100)
    year = models.IntegerField(null=False, blank=False)
