# Generated by Django 3.1.7 on 2021-04-01 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_auto_20210401_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='students',
        ),
    ]