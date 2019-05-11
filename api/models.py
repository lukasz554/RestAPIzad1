from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=120, default='Jan')
    last_name = models.CharField(max_length=45)
