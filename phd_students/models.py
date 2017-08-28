from django.db import models
from employee.models import Employee
# Create your models here.
class PhdStudent(models.Model):
    employee_id = models.ForeignKey(to='Employee',related_name='employee_phd')
    total_student = models.IntegerField()
    awarded = models.IntegerField()
    submitted = models.IntegerField()
    pursuing = models.IntegerField()

    class Meta:
        db_table ='phdstudent'
