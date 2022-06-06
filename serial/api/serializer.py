from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    address = serializers.CharField(max_length=100)
    mobile_number = serializers.IntegerField
