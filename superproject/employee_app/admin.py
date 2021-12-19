from django.contrib import admin
from employee_app.models import Positions, Employees, Payments


@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ["id", "job_title"]


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "position", "salary", "chief"]
    list_display_links = ["full_name", "chief"]
    list_filter = ("position",)


@admin.register(Payments)
class Payments(admin.ModelAdmin):
    list_display = ["id", "employee", "date_time", "accrued"]
    list_display_links = ["employee"]
