# Generated by Django 5.0.6 on 2024-07-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0055_remove_countdownstate_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankdetails',
            name='ifsc_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
