# Generated by Django 5.0.6 on 2024-05-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_citymaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='departmentmaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='designationmaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
