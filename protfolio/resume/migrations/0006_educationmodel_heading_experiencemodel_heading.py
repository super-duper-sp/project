# Generated by Django 4.1 on 2022-09-17 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_educationmodel_experiencemodel_socialmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationmodel',
            name='heading',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='heading',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
