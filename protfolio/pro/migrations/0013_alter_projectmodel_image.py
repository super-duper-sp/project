# Generated by Django 4.2.3 on 2023-09-07 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0012_alter_projectmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
    ]
