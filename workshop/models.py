from django.db import models

# Create your models here.
from employee.models import Employee


class Workshop(models.Model):
    employee_id = models.ForeignKey(to=Employee)
    name = models.CharField(max_length=100)
    date = models.DateField()
    duration = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
