from django.db import models

# Create your models here.


class Students(models.Model):
    f_name = models.CharField(max_length=64)
    l_name = models.CharField(max_length=64)
    birth_date = models.DateField()
    GBA = models.DecimalField(max_digits=3, decimal_places=2)
