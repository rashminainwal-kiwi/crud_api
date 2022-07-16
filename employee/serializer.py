from rest_framework import serializers
import validation_message
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    employee_regNo = serializers.IntegerField(required=True,
                                              error_messages=validation_message.VALIDATION['employee_regNo'])
    employee_name = serializers.CharField(
        required=True, min_length=validation_message.CHAR_LIMIT_SIZE['employee_name_min'],
        max_length=validation_message.CHAR_LIMIT_SIZE['employee_name_max'],
        error_messages=validation_message.VALIDATION['employee_name']
    )

    employee_email = serializers.EmailField(required=True, error_messages=validation_message.VALIDATION['email'])
    employee_mobile = serializers.IntegerField(
        error_messages=validation_message.VALIDATION['employee_mobile']
    )
    created_at = serializers.DateTimeField()

    def validate_employee_email(self, employee_email):
        existing = Employee.objects.filter(employee_email=employee_email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                                              "address has already registered. Was it you?")
        return employee_email

    @staticmethod
    def create(validated_data, password=None):
        details = Employee.objects.create(
            employee_regNo=validated_data['employee_regNo'],
            employee_name=validated_data["employee_name"],
            employee_email=validated_data["employee_email"],
            employee_mobile=validated_data["employee_mobile"],
            created_at=validated_data["created_at"]
        )
        return details

    # def update(self, instance, validated_data):
    #     instance.employee_regNo=
    #     instance.employee_name=
    #     instance.employee_email=
    #     instance.employee_mobile=
    #     instance.created_at=
    #     return instance

    class Meta:
        model = Employee
        fields = '__all__'
