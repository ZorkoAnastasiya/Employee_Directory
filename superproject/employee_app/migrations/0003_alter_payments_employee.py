# Generated by Django 4.0 on 2021-12-21 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_auto_20211219_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='employee_app.employees'),
        ),
    ]
