from django.db import models


# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    GPA = models.DecimalField(max_digits=3, decimal_places=2)




