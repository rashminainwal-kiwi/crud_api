from rest_framework.response import Response
from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework import viewsets, status


class EmployeeAPIView(viewsets.ModelViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    queryset = Employee
    serializer_class = EmployeeSerializer

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return EmployeeSerializer
    #     return EmployeeSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data, context=kwargs)
    #     if serializer.is_valid():
    #         serializer.save()
    #
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Employee.objects.all().order_by('-id')
        serializer = self.get_serializer(queryset, many=True)
        # serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        # serializer = EmployeeSerializer
        # return Response(serializer.data)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        # employee = self.get_object()
        # employee.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        # serializer = EmployeeSerializer
        # return Response(serializer.data)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

