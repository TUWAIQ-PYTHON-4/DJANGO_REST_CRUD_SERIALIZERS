from django.db import models

class student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateTimeField()
    GPA = models.DecimalField(max_digits=2, decimal_places=1)

