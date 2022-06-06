
from rest_framework import serializers
from .models import Cutomer


class CutomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cutomer
        fields = ['id', 'Cutomer_Name', 'Cutomer_id', 'Paid_Amount', 'Address']
