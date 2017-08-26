from django.db import models

# Create your models here.
from employee.models import Employee


class Extra(models.Model):
    employee_id = models.ForeignKey(to=Employee)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    year = models.IntegerField()


    class Meta:
        db_table = 'extras'
