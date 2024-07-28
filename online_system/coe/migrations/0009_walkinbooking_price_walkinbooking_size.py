# Generated by Django 5.0.7 on 2024-07-28 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coe', '0008_category_opportunity_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='walkinbooking',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='walkinbooking',
            name='size',
            field=models.CharField(default='0.00', max_length=255),
            preserve_default=False,
        ),
    ]
