from django.db import models

# Create your models here.
from employee.models import Employee


class Subject(models.Model):
    name = models.CharField(verbose_name = "Subject Name",max_length=100)
    code = models.CharField(verbose_name = "Subject Code",max_length=100)

    class Meta:
        db_table = 'subject'


class SubjectsTaken(models.Model):
    employee = models.ForeignKey(to=Employee , verbose_name='Employee ID')
    subjects = models.TextField(verbose_name="Subject Name", max_length=200)
    year = models.CharField(verbose_name = "Year",max_length=4)
    school = models.CharField("School",max_length=100)
    sem = models.CharField("Semester", max_length=100)
    mode = models.CharField("Type", max_length=100)
    image = models.CharField("File Name", max_length=100, blank=True, null=True)
    course = models.CharField("Course", max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'subjects_taken'
