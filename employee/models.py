from django.db import models


# Create your models here.
class Employee(models.Model):
    employee_regNo = models.IntegerField(unique=True)
    employee_name = models.TextField(unique=True)
    employee_email = models.EmailField(unique=True)
    employee_mobile = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now=True)
