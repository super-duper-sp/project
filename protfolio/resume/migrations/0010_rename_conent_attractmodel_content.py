# Generated by Django 4.1.1 on 2022-09-24 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_attractmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attractmodel',
            old_name='conent',
            new_name='content',
        ),
    ]