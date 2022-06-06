from django.db import models

# Create your models here.


class Student(models.Model):
    Student_Name = models.CharField(max_length=50)
    Roll_No = models.CharField(max_length=40)
    Year = models.IntegerField()
    Branch = models.CharField(max_length=100)
