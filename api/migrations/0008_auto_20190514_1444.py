# Generated by Django 2.2.1 on 2019-05-14 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190514_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='is_working',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
    ]
