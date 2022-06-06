from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField()
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    
