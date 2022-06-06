from django.shortcuts import render
from rest_framework.response import Response
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import viewsets
# Create your views here.


class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        Emp = Employee.objects.all()
        serializer = EmployeeSerializer(Emp, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            Emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(Emp)
        return Response(serializer.data)

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer. is_valid():
            serializer.save()
            return Response({'msg': 'DATA CREATED'})
        return Response(serializer.errors)

    def update(self, request, pk):
        id = pk
        Emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(Emp, data=request.data)
        if serializer. is_valid():
            serializer.save()
            return Response({'msg': 'Complete data updated'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        Emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(Emp, data=request.data, partial=True)
        if serializer. is_valid():
            serializer.save()
            return Response({'msg': 'Partial data updated'})
        return Response(serializer.errors)

    def delete(self, request, pk):
        id = pk
        Emp = Employee.objects.get(pk=id)
        Emp.delete()
        return Response({'Msg': 'DATA DELETED'})
