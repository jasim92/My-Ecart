# Generated by Django 3.1.1 on 2020-09-22 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20200922_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='total_amount',
        ),
    ]
