# Generated by Django 4.0.3 on 2022-07-18 19:29

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0019_alter_schedule_scheduledate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='scheduleDate',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date.today), django.core.validators.MaxValueValidator(datetime.date(2022, 8, 1))]),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='status',
            field=models.CharField(blank=True, choices=[('Confirmed', 'Confirmed'), ('Pending', 'Pending')], max_length=10, null=True),
        ),
    ]
