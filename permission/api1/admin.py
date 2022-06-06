from django.contrib import admin

from api1.views import StudentModelViewSet
from .models import Student

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'Student_Name',
                    'Roll_No', 'Year', 'Branch']
