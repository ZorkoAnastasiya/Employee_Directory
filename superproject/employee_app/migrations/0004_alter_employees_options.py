# Generated by Django 4.0 on 2021-12-23 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("employee_app", "0003_alter_payments_employee"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="employees",
            options={
                "ordering": ["id"],
                "verbose_name": "employee",
                "verbose_name_plural": "employees",
            },
        ),
    ]
