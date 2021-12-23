from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from employee_app.models import Employees
from employee_app.serializers import EmployeesSerializer


class EmployeesViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

