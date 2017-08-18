from django.db import models

# Create your models here.
from employee.models import Employee


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    credit = models.IntegerField()


class SubjectsTaken(models.Model):
    employee_id = models.ForeignKey(to=Employee)
    subjects = models.ManyToManyField(to=Subject)
    year = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
