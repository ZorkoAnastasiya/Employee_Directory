from rest_framework import serializers
from employee_app.models import Employees, Payments


class PaymentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payments
        fields = ["date_time", "accrued"]


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    position = serializers.StringRelatedField()
    chief = serializers.StringRelatedField()
    payments = PaymentsSerializer(many=True, read_only=True)

    class Meta:
        model = Employees
        fields = ["id", "full_name", "date_start", "position", "chief", "salary", "payments"]

