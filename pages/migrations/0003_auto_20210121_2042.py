# Generated by Django 3.1.4 on 2021-01-21 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210111_1812'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='displayUserNames',
        ),
    ]