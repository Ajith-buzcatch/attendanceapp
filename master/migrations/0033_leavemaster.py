# Generated by Django 5.0.6 on 2024-06-11 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0032_alter_attendancemaster_table_alter_citymaster_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='leavemaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaves', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
