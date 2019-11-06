from django.db import models
import datetime

class Student(models.Model):
    class Meta:
        verbose_name_plural = "Students"
    
    code = models.CharField(max_length=12, blank=False,
                            help_text="Code assigned to the student")
    GENDER_TYPES = [
        ('F', "Female"),
        ('M', "Male"),
    ]
    gender = models.CharField(
        max_length=1, choices=GENDER_TYPES, default='M', help_text="Gender")
    first_name = models.CharField(max_length=20, blank=False,
                                  help_text="First name")
    last_name = models.CharField(max_length=20, blank=False,
                                 help_text="Last name")
    birth_date = models.DateField(blank=False, default=datetime.date.today, help_text="Birth date")
    phone_number = models.CharField(max_length=12, blank=True,
                                    help_text="Phone number")

    def __str__(self):
        return "{self.last_name}, {self.first_name}".format(self=self)

class Address(models.Model):
    class Meta:
        verbose_name_plural = "Addresses"
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    ADDRESS_TYPES = [
        ('HOME', "Home"),
        ('Work', "Work"),
        ('FAMILY', "Family"),
    ]
    address_type = models.CharField(max_length=12, choices=ADDRESS_TYPES, blank=False,
                                    help_text="Address type")
    address = models.CharField(max_length=100, blank=False,
                               help_text="Address")
