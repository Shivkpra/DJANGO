from django.shortcuts import render
from .models import Students
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
def student_details(request):
    stu= Students.objects.get(id=1)
    print(stu)
    serializer =StudentSerializer(stu)
    print(serializer)
    json_data=JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')

def student_list(request):
    stu= Students.objects.all()

    serializer =StudentSerializer(stu,many=True)

    json_data=JSONRenderer().render(serializer.data)

    return HttpResponse(json_data,content_type='application/json')



