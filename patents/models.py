from django.db import models

# Create your models here.
from employee.models import Employee


class Patents(models.Model):
    employee_id = models.ForeignKey(to=Employee, related_name='employee_patent')
    name = models.CharField("Patent Name",max_length=100)
    patenting_agency = models.CharField("Patenting Agency",max_length=100)
    year_application = models.IntegerField("Year Of Application")
    year_grant = models.IntegerField("Year of Grant")

    class Meta:
        db_table = 'patents'
