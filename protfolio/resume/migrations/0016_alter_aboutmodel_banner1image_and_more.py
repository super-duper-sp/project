# Generated by Django 4.2.5 on 2023-10-22 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0015_aboutmodel_banner1image_aboutmodel_banner2image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='banner1image',
            field=models.ImageField(blank=True, null=True, upload_to='About/'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='banner2image',
            field=models.ImageField(blank=True, null=True, upload_to='About/'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='banner3image',
            field=models.ImageField(blank=True, null=True, upload_to='About/'),
        ),
    ]
