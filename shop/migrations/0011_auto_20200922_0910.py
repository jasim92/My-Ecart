# Generated by Django 3.1.1 on 2020-09-22 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200922_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(max_length=100),
        ),
    ]