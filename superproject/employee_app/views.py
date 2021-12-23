from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from employee_app.models import Employees
from employee_app.serializers import EmployeesSerializer


class EmployeesViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeesSerializer

    def get_queryset(self):
        queryset = Employees.objects.all()
        level = self.request.query_params.get("level")
        if level is not None:
            result = [obj.id for obj in queryset if obj.level == int(level)]
            queryset = queryset.filter(id__in=result)
        return queryset
