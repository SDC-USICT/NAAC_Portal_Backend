from django.db import models

# Create your models here.
from employee.models import Employee


class JournalPapers(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_jp')
    title_of_paper = models.CharField(max_length=100)
    name_and_publisher = models.CharField(max_length=100)
    volume_no = models.CharField(max_length=100)
    issn_isbn = models.CharField(max_length=100)
    indexing = models.CharField(max_length=100)
    year = models.IntegerField()
    month = models.CharField(max_length=12)
    author = models.ManyToManyField(to=Employee, related_name='employee_jp_author')

    class Meta:
        db_table = 'publication_details'


class Conference(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_conf')
    title_of_paper = models.CharField(max_length=100)
    name_and_publisher = models.CharField(max_length=100)
    volume_no = models.CharField(max_length=100)
    issn_isbn = models.CharField(max_length=100)
    indexing = models.CharField(max_length=100)
    year = models.IntegerField()
    month = models.CharField(max_length=12)
    international_national = models.CharField(max_length=100)
    author = models.ManyToManyField(to=Employee, related_name='employee_conf_author')

    class Meta:
        db_table = 'conference'


class BookChapters(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_book_chapter')
    title_of_paper = models.CharField(max_length=100)
    book_title_and_publisher = models.CharField(max_length=100)
    page_no = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    indexing = models.CharField(max_length=100)
    year = models.IntegerField()
    month = models.CharField(max_length=12)
    author = models.ForeignKey(to=Employee, related_name='employee_book_chapter_author')

    class Meta:
        db_table = 'book_chapters'


class Book(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_book')
    title_of_book = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        db_table = 'book'
