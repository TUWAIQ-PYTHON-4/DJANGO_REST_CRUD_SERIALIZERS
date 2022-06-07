from django.db import models

# Create your models here.
class students(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    GPA = models.FloatField()

