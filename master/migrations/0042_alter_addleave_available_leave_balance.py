# Generated by Django 5.0.6 on 2024-06-26 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0041_addleave_available_leave_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addleave',
            name='available_leave_balance',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
