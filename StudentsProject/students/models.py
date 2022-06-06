from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birth = models.DateField()
    date = models.DateField(auto_now_add=True)
    GPA = models.FloatField()


'''
{
    "firstname": "Bushra",
    "lastname" : "Alzahrani",
    "birth" : "1996-09-24",
    "GPA"  : 4.0
    
    }

'''
