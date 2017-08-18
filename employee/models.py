from django.db import models

# Create your models here.


class Employee(models.Model):

    instructor_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.BigIntegerField()
    date_of_joining = models.DateField(max_length=1000, blank=True, null=True)
    password = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    room_no = models.CharField(max_length=10)
    school = models.CharField(max_length=10)
