from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.


class Employee(models.Model):
    instructor_id = models.CharField(max_length=10, primary_key=True, verbose_name='Employee ID')
    name = models.CharField("Name", max_length=200)
    email = models.EmailField("Email",max_length=200)
    phone = models.BigIntegerField("Phone")
    date_of_joining = models.TextField("Date of Joining", max_length=1000, blank=True, null=True)
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
            school=self.school,
        )

    class Meta:
        db_table = 'employee'


class DontFill(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_fs', default=False)
    awards = models.BooleanField("Awards", default=False)
    extra_activities = models.BooleanField("Extra", default=False)
    guest_lecturer = models.BooleanField("GuestLecturer", default=False)
    moab = models.BooleanField("Membership", default=False)
    patents = models.BooleanField("Patents", default=False)
    professional_details = models.BooleanField("Professional", default=False)
    project = models.BooleanField("Projects", default=False)
    journal_papers = models.BooleanField("JournalPapers", default=False)
    conference = models.BooleanField("Conference", default=False)
    bookchapters = models.BooleanField("BookChapters", default=False)
    book = models.BooleanField("Book", default=False)
    subjects_taken = models.BooleanField("SubjectsTaken", default=False)
    workshop = models.BooleanField("Workshop", default=False)

    class Meta:
        db_table = 'fill_status'
