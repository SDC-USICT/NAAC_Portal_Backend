from django.db import models

# Create your models here.


class Employee(models.Model):

    instructor_id = models.CharField(max_length=10, primary_key=True, verbose_name='Employee ID')
    name = models.CharField("Name", max_length=200)
    email = models.EmailField("Email",max_length=200)
    phone = models.BigIntegerField("Phone")
    date_of_joining = models.DateField("Date of Joining", max_length=1000, blank=True, null=True)
    password = models.CharField("Password", max_length=100)
    designation = models.CharField("Designation", max_length=100)
    room_no = models.CharField("Room No", max_length=10)
    school = models.CharField("School", max_length=10)

    def as_json(self):
        return dict(
            instructor_id=self.instructor_id,
            name=self.name,
            email=self.email,
            phone=self.phone,
            date_of_joining=self.date_of_joining,
            designation=self.designation,
            room_no=self.room_no,
            school=self.school
        )

    class Meta:
        db_table = 'employee'
