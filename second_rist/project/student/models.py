from django.db import models

# Create your models here.

class students(models.Model):
    f_name = models.CharField(max_length=128)
    l_name = models.CharField(max_length=128)
    b_date = models.IntegerField(max_length=128)
    GPA = models.IntegerField(max_length=128)
