# Generated by Django 4.2.4 on 2023-08-13 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_employeedata_delete_employee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmployeeData',
            new_name='Employee',
        ),
    ]