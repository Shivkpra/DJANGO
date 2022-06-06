from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'Cutomer_Name', 'Cutomer_id', 'Paid_Amount', 'Address']
