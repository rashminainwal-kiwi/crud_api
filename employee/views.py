from rest_framework.response import Response
from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework import viewsets, status


class EmployeeAPIView(viewsets.ModelViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    queryset = Employee
    serializer_class = EmployeeSerializer

    # def serializer_class(self):
    #     if self.request.method == 'GET':
    #         return EmployeeSerializer
    #     return EmployeeSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = self.queryset.objects.all()
            return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=kwargs)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        employee_id = self.kwargs['pk']
        queryset = Employee.objects.filter(id=employee_id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        employee_id = self.kwargs['pk']
        queryset = Employee.objects.filter(id=employee_id).first()
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        employee_id = self.kwargs['pk']
        queryset = Employee.objects.filter(id=employee_id).first()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
