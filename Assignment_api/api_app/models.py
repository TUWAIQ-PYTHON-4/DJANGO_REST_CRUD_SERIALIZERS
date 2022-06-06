from django.db import models

class Student(models.Model):
        first_name = models.CharField(max_length=10)
        last_name = models.CharField(max_length=10)
        birthday = models.DateField(max_length=13)
        gpa = models.IntegerField()

        class Meta:
            pass
