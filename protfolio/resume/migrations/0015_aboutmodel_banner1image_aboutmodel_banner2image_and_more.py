# Generated by Django 4.2.5 on 2023-10-14 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0014_aboutmodel_hirelink_aboutmodel_resumelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='banner1image',
            field=models.ImageField(blank=True, null=True, upload_to='About/banner'),
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='banner2image',
            field=models.ImageField(blank=True, null=True, upload_to='About/banner'),
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='banner3image',
            field=models.ImageField(blank=True, null=True, upload_to='About/banner'),
        ),
    ]