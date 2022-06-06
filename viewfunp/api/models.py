from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=50)
    Employee_id=models.CharField(max_length=40)
    Salary=models.IntegerField()
    Address=models.CharField(max_length=100)
