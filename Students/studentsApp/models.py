from django.db import models


# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(blank=True)
    GPA = models.DecimalField(decimal_places=1, max_digits=3)

    def __str__(self):
        return self.first_name
