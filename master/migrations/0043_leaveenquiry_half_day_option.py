# Generated by Django 5.0.6 on 2024-06-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0042_alter_addleave_available_leave_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveenquiry',
            name='half_day_option',
            field=models.TextField(blank=True, null=True),
        ),
    ]
