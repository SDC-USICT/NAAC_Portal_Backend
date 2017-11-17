import datetime
from django.db import models

# Create your models here.
from employee.models import Employee


class Professional(models.Model):
    employee = models.ForeignKey(to=Employee, verbose_name='Employee ID')
    title = models.CharField("Highest Qualification",max_length=100)
    undergraduation_course = models.CharField("Undergraduation Course",max_length=100)
    undergraduation_stream = models.CharField("Undergraduation Stream",max_length=100)
    undergraduation_year = models.CharField("Undergraduation Year",max_length=100,default="null")
    undergraduation_college = models.CharField("Undergraduation College",max_length=100)
    postgraduation_course = models.CharField("Postgraduation Course",max_length=100)
    postgraduation_stream = models.CharField("Postgraduation Stream",max_length=100)
    postgraduation_year = models.CharField("Postgraduation Year",max_length=100,default="null")
    postgraduation_college = models.CharField("Postgraduation College",max_length=100)
    phd_title = models.CharField("PhD Title", max_length=100,default="null")
    phd_specialization = models.CharField("PhD Specialization", max_length=100,default="null")
    phd_college = models.CharField("PhD College", max_length=100,default="null")
    phd_year_application = models.CharField("PhD Year Application", max_length=4,default="")
    phd_year_acquiring = models.CharField("PhD Year Acquiring", max_length=4,default="")
    phd_no = models.BooleanField("No PhD", default=False)
    pdf_title = models.CharField("PDF Title", max_length=100,default="null")
    pdf_specialization = models.CharField("PDF Specialization", max_length=100,default="null")
    pdf_college = models.CharField("PDF College", max_length=100,default="null")
    pdf_year_application = models.CharField("PDF Year Application", max_length=4,default="")
    pdf_year_acquiring = models.CharField("PDF Year Acquiring", max_length=4,default="")
    pdf_no = models.BooleanField("No PdF", default=False)
    acedemic_exp = models.CharField("Acedemic Experience", max_length=4,default="null")
    industrial_exp = models.CharField("Industrial Experience",max_length=100)
    qualification_year_completion = models.CharField("Year Of Completion of Highest Qualification",max_length=100,default="null")
    pursuing = models.IntegerField("Phd Pursuing",default=0)
    submitted = models.IntegerField("Phd Submitted",default=0)
    awarded = models.IntegerField("Phd Awarded",default=0)
    phds = models.IntegerField("Total Student",default=0)


    class Meta:
        db_table = 'professional'
