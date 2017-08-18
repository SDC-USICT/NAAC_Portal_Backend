from django.db import models

# Create your models here.
from employee.models import Employee


class Projects(models.Model):
    employee_id = models.ForeignKey(to=Employee, related_name='employee_projects')
    title = models.CharField(max_length=100)
    pi = models.ForeignKey(to=Employee, related_name='employee_pi')
    copi = models.ManyToManyField(to=Employee, related_name='employee_copi')
    sponsors = models.CharField(max_length=100)
    date_of_award = models.DateField()
    date_completed = models.DateField()
    amnt_sanctioned = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
