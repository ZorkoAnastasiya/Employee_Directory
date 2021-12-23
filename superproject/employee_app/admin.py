from django.contrib import admin
from employee_app.models import Positions, Employees, Payments


class LevelEmployeeListFilter(admin.SimpleListFilter):
    title = "Level Employees"
    parameter_name = "level"

    def lookups(self, request, model_admin):
        return [
            ("1", "Level 1"),
            ("2", "Level 2"),
            ("3", "Level 3"),
            ("4", "Level 4"),
            ("5", "Level 5")
        ]

    def queryset(self, request, queryset):
        if self.value() in ["1", "2", "3", "4", "5"]:
            result = [obj.id for obj in queryset if obj.level == int(self.value())]
            return queryset.filter(id__in=result)


@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ("id", "job_title")
    list_display_links = ("job_title",)


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "position", "view_chief", "salary", "total_paid")
    list_display_links = ("full_name",)
    list_filter = ("position", LevelEmployeeListFilter)
    date_hierarchy = "date_start"
    actions = ["delete_total_paid"]

    @admin.action(description="Delete all payments")
    def delete_total_paid(self, request, queryset):
        for obj in queryset:
            result = obj.payments.all()
            result.delete()

    def view_chief(self, obj):
        from django.utils.html import format_html
        from django.urls import reverse
        from django.utils.http import urlencode
        url = (
                reverse("admin:employee_app_employees_changelist")
                + "?"
                + urlencode({"id": f"{obj.chief_id}"})
        )
        return format_html(
            "<a href='{url_id}'>{url_name}</a>",
            url_id=url,
            url_name=obj.chief
        )

    view_chief.short_description = "Chief"

    @staticmethod
    def total_paid(obj):
        from django.db.models import Sum
        result = obj.payments.aggregate(Sum("accrued"))
        return result["accrued__sum"]


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("id", "employee", "date_time", "accrued")
    list_display_links = ("employee",)
    list_filter = ("employee",)
    date_hierarchy = "date_time"
