from django.db import models

# Create your models here.
from employee.models import Employee


class Awards(models.Model):
    employee_id = models.ForeignKey(to=Employee, related_name='employee_awards')
    title = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    year = models.IntegerField()
