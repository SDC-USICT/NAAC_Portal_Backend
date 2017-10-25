from django.db import models

# Create your models here.
from employee.models import Employee


class Projects(models.Model):
    employee = models.ForeignKey(to=Employee, related_name='employee_projects', verbose_name='Employee ID')
    title = models.CharField("Project Title",max_length=100)
    sponsors = models.TextField("Sponsoring Agency")
    date_of_award = models.TextField("Date of Award")
    date_completed = models.TextField("Date of Completed")
    amnt_sanctioned = models.IntegerField("Amount Sanctioned")
    status = models.CharField("Status",max_length=100)
    author = models.CharField(max_length=200, verbose_name='Principle Investigator', blank=True, null=True)
    coauthor = models.TextField(max_length=200, verbose_name='Co Principle Investigators', blank=True,null=True)


    class Meta:
        db_table = 'project'
