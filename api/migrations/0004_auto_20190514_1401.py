# Generated by Django 2.2.1 on 2019-05-14 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190514_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobposition',
            name='date',
        ),
        migrations.RemoveField(
            model_name='jobposition',
            name='last_update',
        ),
    ]