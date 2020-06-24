from rest_framework import  serializers
from bankapp.models import Bankprofile
from django.contrib.auth.models import User
class BankprofileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Bankprofile
        fields = ('state','bank_name','owner')   #fields='__all__' used for all field  as per model

class UserSerializer(serializers.ModelSerializer):
    Bankprofiles = serializers.PrimaryKeyRelatedField(many=True,queryset=Bankprofile.objects.all())
    class Meta():
        model = User
        fields = ['id','username','Bankprofiles']