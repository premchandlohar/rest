from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from empapp.models import Employee
from .serializers import EmployeeSerializer,UserSerializer,GroupSerializer
from django.contrib.auth.models import User,Group
from rest_framework import permissions



# Create your views here.

class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # -------------------------------------------------------------------------------------------------

class UserViewSet(ModelViewSet):
    # lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    Permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]
    # -------------------------------------------------------------------------------------------------

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    Permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]

    # -------------------------------------------------------------------------------------------------
    


