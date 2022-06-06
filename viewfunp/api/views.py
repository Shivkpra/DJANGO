from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializer import EmployeeSerializer

# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def Employee_api(request,pk=None):
    if request.method =='GET':
        id=pk
        if id is not None:
            Emp=Employee.objects.get(id=id)
            serializer =EmployeeSerializer(Emp)
            return Response(serializer.data)
        Emp= Employee.objects.all()
        serializer = EmployeeSerializer(Emp,many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer =EmployeeSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response({'msg':'DATA CREATED'})
        return Response(serializer.errors)
    if request.method =='PUT':
        id=pk
        Emp=Employee.objects.get(pk=id)
        serializer=EmployeeSerializer(Emp,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'DATA UPADATED'})
        return Response(serializer.errors)
    if request.method == 'PATCH':
        id = pk
        Emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(Emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'PDATA UPADATED'})
        return Response(serializer.errors)

    if request.method =='DELETE':
        id = pk
        Emp = Employee.objects.get(pk=id)
        Emp.delete()
        return Response({'msg':'DATA DELETED'})