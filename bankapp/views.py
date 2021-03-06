from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import  reverse
# from rest_framework.permissions import IsAdminUser

import json
from .models import Bankprofile
from validator import *
from django.db import transaction

class bankprofilelist(APIView):
    # Permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]#testing purpose comment

    def get(self,request):
        bankprofile1 = Bankprofile.objects.all()
        serializer = BankprofileSerializer(bankprofile1,many=True)
        return Response(serializer.data)

    
    def post(self,request):
        serializer = BankprofileSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

# ---------------------------------------------------------------------------------------------

class Banklist(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Bankprofile.objects.all()
    serializer_class = BankprofileSerializer

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class Bankdetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = bankprofile1 = Bankprofile.objects.all()
    serializer_class = BankprofileSerializer
# --------------------------------------------------------------------------------------------------

class Userlist(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]

class Userdetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # --------------------------------------------------------------------------------------------------

class ApiRoot(APIView):
    def get(self,request):
        return Response({
            # 'bankprofile': reverse('bankprofile',request=request),
            'banks': reverse('banks',request=request),
            'users': reverse('users',request=request) 
        })




# Create your views here.
# def establish_new_bank(request):
#     params = json.loads(request.body)

#     state = params.get('state')
#     bank_name = params.get('bank_name')
#     ifsc_code = params.get('ifsc_code')
#     branch = params.get('branch')
#     address = params.get('address')
#     contact = params.get('contact')
#     city = params.get('city')
#     district = params.get('district')

#     #valided there fields
#     try:
#         if valid_string(state):return JsonResponse({'validation':'enter valid state ,must be a string'})   
#         elif valid_string(bank_name):return JsonResponse({'validation':'enter valid bank_name,must be a string'})  
#         elif valid_ifsc_code(ifsc_code):return JsonResponse({'validation':'enter valid ifsc_code,must be a string & digit must be 11'})   
#         elif valid_string(branch):return JsonResponse({'validation':'enter valid branch,must be a string'})    
#         elif valid_string(address):return JsonResponse({'validation':'enter valid address,must be a string'})
#         elif valid_mobile_number(contact):return JsonResponse({'validation':'enter valid contact ,must be a string and 10 digit'})   
#         elif valid_string(city):return JsonResponse({'validation':'enter valid city ,must be a string'})   
#         elif valid_string(district):return JsonResponse({'validation':'enter valid district,must be a string'})   
        
#         with transaction.atomic():#used for all field is valid then and only then create obj
#             bank_obj = Bankprofile.objects.create(#create the details
#                 state = state,
#                 bank_name = bank_name,
#                 ifsc_code = ifsc_code,
#                 branch = branch,
#                 address = address,
#                 contact = contact,
#                 city = city,
#                 district = district
#             )
#             return JsonResponse({'validation':'success','status':True})
#     except Exception as e:
#         return JsonResponse({'validation':str(e),'status':False})
#         # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def update_bank_details(request):
#     params = json.loads(request.body)

#     bank_id = params.get('bank_id')
#     state = params.get('state')
#     bank_name = params.get('bank_name')
#     ifsc_code = params.get('ifsc_code')
#     branch = params.get('branch')
#     address = params.get('address')
#     contact = params.get('contact')
#     city = params.get('city')
#     district = params.get('district')

#     try:
#         if valid_integer(bank_id):return JsonResponse({'validation':'enter valid bank_id ,must be a integer'})   
#         elif valid_string(state):return JsonResponse({'validation':'enter valid state ,must be a string'})   
#         elif valid_string(bank_name):return JsonResponse({'validation':'enter valid bank_name,must be a string'})  
#         elif valid_ifsc_code(ifsc_code):return JsonResponse({'validation':'enter valid ifsc_code,must be a string & digit must be 11'})   
#         elif valid_string(branch):return JsonResponse({'validation':'enter valid branch,must be a string'})    
#         elif valid_string(address):return JsonResponse({'validation':'enter valid address,must be a string'})
#         elif valid_mobile_number(contact):return JsonResponse({'validation':'enter valid contact ,must be a string and 10 digit'})   
#         elif valid_string(city):return JsonResponse({'validation':'enter valid city ,must be a string'})   
#         elif valid_string(district):return JsonResponse({'validation':'enter valid district,must be a string'})   
        
#         with transaction.atomic():
#             bank_obj = Bankprofile.objects.get(id = bank_id)
#             bank_obj.state = state
#             bank_obj.bank_name = bank_name
#             bank_obj.ifsc_code = ifsc_code
#             bank_obj.branch = branch
#             bank_obj.address = address
#             bank_obj.contact = contact
#             bank_obj.city = city
#             bank_obj.district = district
#             bank_obj.save()
#             return JsonResponse({'validation':'success','status':True})
            
#     except Exception as e:
#         return JsonResponse({'validation':str(e),'status':False})
#         # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def get_bank_details_by_ifsc_code(request):
#     params = json.loads(request.body)
#     response = []

#     ifsc_code = params.get('ifsc_code')

#     #valided the ifsc code
#     if valid_ifsc_code(ifsc_code):return JsonResponse({'validation':'enter valid ifsc_code,must be a string & digit must be 11'})   
#     try:
#         bank_obj = Bankprofile.objects.get(ifsc_code=ifsc_code)#create object of specific bank
#         # print(bank_obj)
#         if bank_obj:#if object is true then append a there field into response list
#             response.append({
#                 "state":bank_obj.state,
#                 "bank_name":bank_obj.bank_name,
#                 "ifsc_code":bank_obj.ifsc_code,
#                 "branch":bank_obj.branch,
#                 "address":bank_obj.address,
#                 "contact":bank_obj.contact,
#                 "city":bank_obj.city,
#                 "district":bank_obj.district
#             })
#             return JsonResponse({'validation':'success','response':response,'status':True})

#         else:
#             return JsonResponse({'validation':'please enter a valid ifsc_code','status':False})

#     except Exception as e:
#         return JsonResponse({'validation':str(e),'status':False})
#         # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def get_all_bank_details(request):
#     response = []

#     try:
#         bank_obj = Bankprofile.objects.all()
#         for bank in bank_obj:
#             response.append({ 
#                 "bank_id":bank.id,
#                 "state":bank.state,
#                 "bank_name":bank.bank_name,
#                 "ifsc_code":bank.ifsc_code,
#                 "branch":bank.branch,
#                 "address":bank.address,
#                 "contact":bank.contact,
#                 "city":bank.city,
#                 "district":bank.district
#             })
#         return JsonResponse({'validation':'success','response':response,'status':True})

#     except Exception as e:
#         return JsonResponse({'validation':str(e),'status':False})
#         # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def terminate_bank(request):
#     params = json.loads(request.body)

#     bank_id = params.get('bank_id')

#     if valid_integer(bank_id):return JsonResponse({'validation':'enter valid bank_id,must be integer'})   

#     try:
#         obj = Bankprofile.objects.get(id=bank_id).delete()
#         return JsonResponse({'validation':'success','response':'terminate this branch','status':True})

#     except Exception as e:
#         return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


