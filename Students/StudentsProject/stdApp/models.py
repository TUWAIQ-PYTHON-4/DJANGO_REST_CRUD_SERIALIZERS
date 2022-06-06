from datetime import datetime
from django.db import models

# Create your models here.

class StudentModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True)
    GPA = models.DecimalField(max_digits=3, decimal_places=2)