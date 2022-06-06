from datetime import datetime

from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birthdate = models.DateTimeField(datetime)
    GPA = models.DecimalField(max_digits=3, decimal_places=2)
