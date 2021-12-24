from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication

from employee_app.models import Employees
from employee_app.permissions import IsManagerAuthenticated
from employee_app.serializers import EmployeesSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsManagerAuthenticated,)
    serializer_class = EmployeesSerializer

    def get_queryset(self) -> list[object]:
        """
        Returns a list of all objects.
        If specified, the "level" query parameter returns a list of objects of the given level.
        """

        queryset = Employees.objects.all()
        level = self.request.query_params.get("level")
        if level is not None:
            result = [obj.id for obj in queryset if obj.level == int(level)]
            queryset = queryset.filter(id__in=result)
        return queryset
