# Generated by Django 5.0.6 on 2024-07-18 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0053_rename_emergency_contact_person_employeeprofile_guardian_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='guardian_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
