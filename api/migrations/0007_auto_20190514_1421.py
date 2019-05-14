# Generated by Django 2.2.1 on 2019-05-14 14:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_jobposition_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposition',
            name='phone',
            field=models.BigIntegerField(default=1000000000000, validators=[django.core.validators.MinValueValidator(100000000), django.core.validators.MaxValueValidator(99999999999999)]),
        ),
    ]