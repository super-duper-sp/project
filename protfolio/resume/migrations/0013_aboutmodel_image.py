# Generated by Django 4.2.5 on 2023-10-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_rename_attractmodel_aboutmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='About/'),
        ),
    ]