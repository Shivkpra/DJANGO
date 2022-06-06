from django.db import models

# Create your models here.


class Employee(models.Model):
    Name = models.CharField(max_length=50)
    Cutomer_id = models.CharField(max_length=40)
    Paid_Amount = models.IntegerField()
    Address = models.CharField(max_length=100)
