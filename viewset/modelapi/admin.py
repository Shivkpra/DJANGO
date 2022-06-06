from django.contrib import admin
from .models import Cutomer

# Register your models here.


@admin.register(Cutomer)
class CutomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'Cutomer_Name',
                    'Cutomer_id', 'Paid_Amount', 'Address']
