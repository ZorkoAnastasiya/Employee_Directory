from rest_framework import serializers

from employee_app.models import Employees


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    position = serializers.StringRelatedField()
    chief = serializers.StringRelatedField()
    total_paid = serializers.SerializerMethodField()

    class Meta:
        model = Employees
        fields = [
            "id",
            "full_name",
            "date_start",
            "position",
            "chief",
            "salary",
            "total_paid",
        ]

    @staticmethod
    def get_total_paid(obj):
        from django.db.models import Sum

        return obj.payments.aggregate(Sum("accrued"))
