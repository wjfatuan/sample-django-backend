from django.db import models
import datetime

class JobTitle(models.Model):
    class Meta:
        verbose_name_plural = "Job Titles"
    name = models.CharField(max_length=30, blank=False, help_text="Job name")
    description = models.TextField(max_length=300, blank=False, help_text="Job description")

    def __str__(self):
        return "{id}:{name}".format(id=self.id, name=self.name)

class Faculty(models.Model):
    class Meta:
        verbose_name_plural = "Faculties"
    code = models.CharField(max_length=12, blank=False,
                            help_text="Code assigned to the faculty")
    GENDER_TYPES = [
        ('F', "Female"),
        ('M', "Male"),
    ]
    gender = models.CharField(
        max_length=1, choices=GENDER_TYPES, blank=False, help_text="Gender")
    first_name = models.CharField(max_length=20, blank=False,
                                  help_text="First name")
    last_name = models.CharField(max_length=20, blank=False,
                                 help_text="Last name")
    birth_date = models.DateField(blank=False, default=datetime.date.today, help_text="Birth date")
    phone_number = models.CharField(max_length=12, blank=True,
                                    help_text="Phone number")
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)

class Subject(models.Model):
    class Meta:
        verbose_name_plural = "Subjects"
    code = models.CharField(max_length=12, blank=True,
                            help_text="Subject code")
    name = models.CharField(max_length=50, blank=True,
                            help_text="Subject name")
