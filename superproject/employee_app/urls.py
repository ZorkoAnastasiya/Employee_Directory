from django.urls import path, include
from rest_framework import routers
from employee_app.views import EmployeesViewSet

router = routers.DefaultRouter()
router.register(r'employees', viewset=EmployeesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]