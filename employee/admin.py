from django.contrib import admin

from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_regNo', 'employee_name', 'employee_email', 'employee_mobile', 'created_at')
