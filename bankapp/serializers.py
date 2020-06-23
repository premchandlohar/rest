from rest_framework import  serializers
from .models import Bankprofile

class BankprofileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bankprofile
        fields = ('state','bank_name')   #fields='__all__' used for all field  as per model