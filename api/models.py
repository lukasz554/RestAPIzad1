from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
import datetime


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(default="")
    phone = models.BigIntegerField(default=1000000000000,
                                   validators=[
                                       MinValueValidator(100000000),
                                       MaxValueValidator(999999999999999)])

    last_update = models.DateField(auto_now=True)
    is_working = models.BooleanField(default=False)
    comment = models.TextField


class JobPosition(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)
