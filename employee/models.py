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
