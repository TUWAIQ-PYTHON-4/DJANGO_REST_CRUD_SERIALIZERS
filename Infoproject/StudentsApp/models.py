from django.db import models

class StudentsInfo(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    birth_date = models.DateField()
    GPA = models.DecimalField(max_digits=3, decimal_places=2)