# Generated by Django 4.2.5 on 2023-10-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_aboutmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='hireLink',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='resumeLink',
            field=models.TextField(blank=True, null=True),
        ),
    ]