# Generated by Django 5.0.6 on 2024-05-28 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0021_alter_employeejoinmaster_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeimage',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_images', to='master.employeemaster'),
        ),
    ]
