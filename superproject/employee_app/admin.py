from django.contrib import admin
from employee_app.models import Positions, Employees, Payments


@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ["id", "job_title"]
    list_display_links = ["job_title"]


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "position", "chief", "salary", "total_paid"]
    list_display_links = ["full_name", "chief"]
    list_filter = ("position",)
    date_hierarchy = "date_start"
    actions = ["delete_total_paid"]

    @admin.action(description="Delete all payments")
    def delete_total_paid(self, request, queryset):
        for obj in queryset:
            result = obj.payments.all()
            result.delete()

    @staticmethod
    def total_paid(obj):
        from django.db.models import Sum
        result = obj.payments.aggregate(Sum("accrued"))
        return result["accrued__sum"]


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ["id", "employee", "date_time", "accrued"]
    list_display_links = ["employee"]
    list_filter = ("employee",)
    date_hierarchy = "date_time"
