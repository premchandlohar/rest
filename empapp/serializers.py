from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import Employee
from django.contrib.auth.models import User,Group
from rest_framework import permissions

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__' 
        # --------------------------------------------------------------------------------------------

class UserSerializer(HyperlinkedModelSerializer):
    class Meta():
        model = User
        fields = ['username','email','first_name']
        # ------------------------------------------------------------------------------------------------

class GroupSerializer(HyperlinkedModelSerializer):
    class Meta():
        model = Group
        fields = ['name']