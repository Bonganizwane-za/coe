# Generated by Django 5.0.7 on 2024-07-28 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coe', '0003_alter_opportunity_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='resources',
        ),
    ]
