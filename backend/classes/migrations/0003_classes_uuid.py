# Generated by Django 3.1.7 on 2021-04-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_sheduletime_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='uuid',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
