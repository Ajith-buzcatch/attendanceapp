# Generated by Django 5.0.6 on 2024-05-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0010_attendancemaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeimage',
            name='employee_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/employee_images'),
        ),
    ]
