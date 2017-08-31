from django.db import models

# Create your models here.
from employee.models import Employee


class Awards(models.Model):
    employee_id = models.ForeignKey(to=Employee, related_name='employee_awards', verbose_name='Employee ID')
    title = models.CharField("Title",max_length=100)
    organisation = models.CharField("Organization",max_length=100)
    month = models.CharField("Month",max_length=100)
    year = models.IntegerField("Year")

    class Meta:
        db_table = 'awards'
