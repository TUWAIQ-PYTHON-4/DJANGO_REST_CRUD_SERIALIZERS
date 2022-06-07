from django.db import models

# Create your models here.

class Students(models.Model):
    firstname=models.CharField(max_length=128)
    lastname=models.CharField(max_length=128)
    GPA = models.DecimalField(max_digits=3, decimal_places=1)
    birth_date = models.DateField()
