# Generated by Django 3.0.5 on 2022-02-23 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.CharField(max_length=200, null=True)),
                ('report', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.Doctors')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.Patient')),
            ],
        ),
    ]
