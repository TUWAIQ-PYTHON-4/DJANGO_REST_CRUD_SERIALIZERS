from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birth_date = models.DateTimeField(auto_now_add=True)
    GPA = models.DecimalField(max_digits=3, decimal_places=2)
