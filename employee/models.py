from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class EmployeeManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The password must be set')
        if not extra_fields['instructor_id']:
            raise ValueError('Instructor ID is not set')

        email = self.normalize_email(email)
        user = self.model(email=email,  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_allowed', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Employee(AbstractBaseUser, PermissionsMixin):
    instructor_id = models.CharField(max_length=10, primary_key=True, verbose_name='Employee ID')
    name = models.CharField("Name", max_length=200)
    email = models.EmailField("Email",max_length=200)
    phone = models.BigIntegerField("Phone", blank=True, null=True)
    date_of_joining = models.TextField("Date of Joining", max_length=1000, blank=True, null=True)
    password = models.CharField("Password", max_length=100)
    designation = models.CharField("Designation", max_length=100)
    room_no = models.CharField("Room No", max_length=10)
    school = models.CharField("School", max_length=10)
    salt = models.TextField(blank=True, null=True)
    csrf_token = models.CharField("CSRF Token", max_length=20, default="null")

    #new argument
    is_active = models.BooleanField(default=True)
    is_allowed = models.BooleanField(default=False, blank=True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['password', 'email']
    USERNAME_FIELD = 'instructor_id'
    EMAIL_FIELD='email'

    objects = EmployeeManager()

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
    employee = models.ForeignKey(Employee, related_name='employee_fs', primary_key=True, on_delete=models.PROTECT)
    awards = models.BooleanField("Awards", default=False)
    extra = models.BooleanField("Extra", default=False)
    guest_lecture = models.BooleanField("GuestLecturer", default=False)
    membership = models.BooleanField("Membership", default=False)
    patents = models.BooleanField("Patents", default=False)
    professional = models.BooleanField("Professional", default=False)
    projects = models.BooleanField("Projects", default=False)
    journal_papers = models.BooleanField("JournalPapers", default=False)
    conference = models.BooleanField("Conference", default=False)
    book_chapters = models.BooleanField("BookChapters", default=False)
    book = models.BooleanField("Book", default=False)
    subjects_taken = models.BooleanField("SubjectsTaken", default=False)
    workshop = models.BooleanField("Workshop", default=False)

    class Meta:
        db_table = 'fill_status'
