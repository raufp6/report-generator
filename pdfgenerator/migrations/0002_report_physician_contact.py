# Generated by Django 5.0.3 on 2024-03-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfgenerator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='physician_contact',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
