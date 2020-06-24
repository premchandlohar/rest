from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('emp',EmployeeCRUDCBV, basename='emp')
router.register(r'users',UserViewSet,basename='users')
router.register('groups',GroupViewSet, basename='groups')


urlpatterns = [
    path('api/',include(router.urls)),#for routers shown above emp,users,groups
    
]
