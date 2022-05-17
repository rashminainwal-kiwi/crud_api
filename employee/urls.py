from django.urls import path
from .views import EmployeeCreateApi, EmployeeUpdateApi, EmployeeDeleteApi,EmployeeApi

urlpatterns = [

    path('', EmployeeCreateApi.as_view()),
    path('list/', EmployeeApi.as_view()),
    path('update/<int:pk>', EmployeeUpdateApi.as_view()),
    path('delete/<int:pk>', EmployeeDeleteApi.as_view()),

]
