# Generated by Django 2.0 on 2019-08-17 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boy',
            old_name='nikename',
            new_name='nickname',
        ),
        migrations.RenameField(
            model_name='girl',
            old_name='nikename',
            new_name='nickname',
        ),
    ]