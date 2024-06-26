# Generated by Django 4.2.1 on 2024-03-30 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(default='Clinet name', max_length=100)),
                ('logo', models.FileField(upload_to='logos/')),
                ('physician_name', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_dob', models.DateField(blank=True, null=True)),
                ('patient_contact', models.CharField(blank=True, max_length=15, null=True)),
                ('chief_complaint', models.CharField(blank=True, max_length=5000, null=True)),
                ('consultation_note', models.CharField(blank=True, max_length=5000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateField(blank=True, null=True)),
                ('added_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reports',
                'ordering': ['-id'],
            },
        ),
    ]
