from django.db import models

# Create your models here.
from employee.models import Employee


class Projects(models.Model):
    employee_id = models.ForeignKey(to=Employee, related_name='employee_projects', verbose_name='Employee ID')
    title = models.CharField("Project Title",max_length=100)
    pi = models.ForeignKey(to=Employee, related_name='employee_pi', verbose_name='Author')
    copi = models.ManyToManyField(to=Employee, related_name='employee_copi', verbose_name='Co Author')
    sponsors = models.CharField("Sponsoring Agency",max_length=100)
    date_of_award = models.DateField("Date of Award")
    date_completed = models.DateField("Date of Completed")
    amnt_sanctioned = models.CharField("Amount Sanctioned",max_length=100)
    status = models.CharField("Status",max_length=100)

    class Meta:
        db_table = 'project'
