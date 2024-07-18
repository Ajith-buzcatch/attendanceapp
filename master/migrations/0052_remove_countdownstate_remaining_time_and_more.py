# Generated by Django 5.0.6 on 2024-07-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0051_remove_countdownstate_total_seconds_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countdownstate',
            name='remaining_time',
        ),
        migrations.AddField(
            model_name='countdownstate',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='countdownstate',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='countdownstate',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
