# Generated by Django 4.0.2 on 2022-04-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_alter_appointment_sent_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='sent_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]