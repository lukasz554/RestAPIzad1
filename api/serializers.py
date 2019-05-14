from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee, JobPosition


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'email', 'phone',
                  'last_update', 'is_working')


class JobPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobPosition
        fields = ('id', 'name', 'date', 'last_update')
