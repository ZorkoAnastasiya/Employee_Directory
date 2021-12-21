from rest_framework import viewsets
from employee_app.models import Employees
from employee_app.serializers import EmployeesSerializer


class EmployeesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

