from django.contrib import admin
from .models import Students

# Register your models here.
@admin.register(Students)
class Student_admin(admin.ModelAdmin):
    list=['id','name','roll','address', 'mobile_number']
