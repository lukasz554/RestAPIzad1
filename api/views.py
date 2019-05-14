from django.contrib.auth.models import User
from rest_framework import viewsets

from api.serializers import UserSerializer
from .models import Employee, JobPosition
from .serializers import EmployeeSerializer, JobPositionSerializer


class UserViewSet(viewsets.ModelViewSet):
        queryset = User.objects.all().order_by('-date_joined')
        serializer_class = UserSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class JobPositionViewSet(viewsets.ModelViewSet):
    queryset = JobPosition.objects.all()
    serializer_class =  JobPositionSerializer
