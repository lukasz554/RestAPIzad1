# Generated by Django 2.2.1 on 2019-05-14 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20190514_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
        migrations.AlterField(
            model_name='jobposition',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 5, 14, 16, 9, 24, 563625)),
        ),
        migrations.AlterField(
            model_name='jobposition',
            name='last_update',
            field=models.DateField(default=datetime.datetime(2019, 5, 14, 16, 9, 24, 563651)),
        ),
    ]
