from django.contrib import admin
from .models import Employee

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'Cutomer_Name',
                    'Cutomer_id', 'Paid_Amount', 'Address']