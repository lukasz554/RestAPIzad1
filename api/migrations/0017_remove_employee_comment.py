# Generated by Django 2.2.1 on 2019-05-14 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20190514_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='comments',
        ),
    ]
