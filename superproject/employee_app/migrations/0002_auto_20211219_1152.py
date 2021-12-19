# Generated by Django 4.0 on 2021-12-19 08:52

from django.db import migrations


def add_title_positions(apps, schema_editor):
    positions_name = [
        "General Manager",
        "Development Director",
        "Commercial Director",
        "Head of Research Department",
        "Technical Director",
        "Chief Accountant",
        "Marketing Director",
        "Head of Development Department",
        "Senior Analyst",
        "System Administrator",
        "Economist",
        "Accountant",
        "Head of Sales Department",
        "Head of Advertising Department",
        "Programmer",
        "Analyst",
        "Junior Accountant",
        "Sales Manager",
        "Advertising Manager",
    ]
    positions = apps.get_model("employee_app", "Positions")
    for name in positions_name:
        position_title = positions(job_title=name)
        position_title.save()


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_title_positions),
    ]