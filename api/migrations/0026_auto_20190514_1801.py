# Generated by Django 2.2.1 on 2019-05-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20190514_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_update',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='jobposition',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='jobposition',
            name='last_update',
            field=models.DateField(auto_now=True),
        ),
    ]