# Generated by Django 5.0.6 on 2024-06-07 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0030_attendancemaster_is_pending_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemaster',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.companydetails'),
        ),
    ]
