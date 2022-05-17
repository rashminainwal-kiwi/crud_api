from django.db import models


# Create your models here.
class Employee(models.Model):
    employee_regNo = models.IntegerField(unique=True)
    employee_name = models.TextField()
    employee_email = models.EmailField()
    employee_mobile = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now=True)
