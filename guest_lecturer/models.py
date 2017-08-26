from django.db import models

# Create your models here.
from employee.models import Employee


class GuestLecturer(models.Model):
    employee = models.ForeignKey(to=Employee, related_name='employee', verbose_name='Employee ID')
    nature = models.CharField("Nature",max_length=100)
    institute = models.CharField("Institute Name",max_length=100)
    date = models.TextField("Date", blank=True, null=True)
    title = models.CharField("Topic",max_length=100)
    year = models.TextField("Year", max_length="4", blank=True, null=True)

    class Meta:
        db_table = 'guest_lecturer'

