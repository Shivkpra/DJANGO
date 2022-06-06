from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    address=models.CharField(max_length=100)
    mobile_number=models.IntegerField

