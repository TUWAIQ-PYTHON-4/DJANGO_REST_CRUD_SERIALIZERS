from django.db import models

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    birth_date=models.DateField()
    GPA=models.FloatField()

    def __str__(self) -> str:
        return self.first_name
