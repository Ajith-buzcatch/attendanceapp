# Generated by Django 5.0.6 on 2024-06-11 04:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0033_leavemaster'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelTable(
            name='leavemaster',
            table='leavemaster',
        ),
        migrations.CreateModel(
            name='leaveenquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slno', models.IntegerField(blank=True, null=True)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('enquery_date', models.DateField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.companydetails')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.employeemaster')),
                ('leave', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.leavemaster')),
                ('submitted_to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
