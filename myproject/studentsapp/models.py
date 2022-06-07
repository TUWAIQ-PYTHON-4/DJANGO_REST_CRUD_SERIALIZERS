from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=128)
    second_name= models.CharField(max_length=128)
    birth_date = models.DateField()
    gpa = models.DecimalField(max_digits=3,decimal_places=2)

