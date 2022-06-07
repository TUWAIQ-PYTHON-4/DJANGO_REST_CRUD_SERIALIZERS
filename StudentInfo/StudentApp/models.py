from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birth_date=models.DateField()
    GPA=models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ('-GPA',)
