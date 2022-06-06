from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.


class EmployeeAPI(APIView):
    def get(self, request, pk=None, format=None):

        id = pk
        if id is not None:
            Emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(Emp)
            return Response(serializer.data)
        Emp = Employee.objects.all()
        serializer = EmployeeSerializer(Emp, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'DATA CREATED'})
        return Response(serializer.errors)

    def put(self, request, pk=None, format=None):
        id = pk
        Emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(Emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'DATA UPADATED'})
        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):
        id = pk
        Emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(Emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'PDATA UPADATED'})
        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):
        id = pk
        Emp = Employee.objects.get(pk=id)
        Emp.delete()
        return Response({'msg': 'DATA DELETED'})
