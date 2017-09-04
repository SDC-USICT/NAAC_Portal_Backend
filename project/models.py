from django.db import models

# Create your models here.
from employee.models import Employee


class Projects(models.Model):
    employee = models.ForeignKey(to=Employee, related_name='employee_projects', verbose_name='Employee ID')
    title = models.CharField("Project Title",max_length=100)
    author = models.ManyToManyField(to=Employee, related_name='employee_copi', verbose_name='Co Authors')
    sponsors = models.CharField("Sponsoring Agency",max_length=100)
    date_of_award = models.TextField("Date of Award")
    date_completed = models.TextField("Date of Completed")
    amnt_sanctioned = models.CharField("Amount Sanctioned",max_length=100)
    status = models.CharField("Status",max_length=100)

    class Meta:
        db_table = 'project'
