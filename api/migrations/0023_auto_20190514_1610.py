# Generated by Django 2.2.1 on 2019-05-14 16:10

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20190514_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.BigIntegerField(default=1000000000000, validators=[django.core.validators.MinValueValidator(100000000), django.core.validators.MaxValueValidator(999999999999999)]),
        ),
        migrations.AlterField(
            model_name='jobposition',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 5, 14, 16, 10, 28, 570347)),
        ),
        migrations.AlterField(
            model_name='jobposition',
            name='last_update',
            field=models.DateField(default=datetime.datetime(2019, 5, 14, 16, 10, 28, 570371)),
        ),
    ]
