
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'jobposition', views.JobPositionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]