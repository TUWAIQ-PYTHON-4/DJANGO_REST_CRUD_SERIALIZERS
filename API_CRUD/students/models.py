from django.db import models


# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    birthdate = models.DateField()
    GPA = models.DecimalField(max_digits=3, decimal_places=2)
