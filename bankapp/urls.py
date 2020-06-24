from django.urls import path
from .views import *

urlpatterns = [
    path('',ApiRoot.as_view(),name='root'),
    path('bankprofile/', bankprofilelist.as_view()),#for bank apiview
    path('banks/', Banklist.as_view(),name='banks'),
    path('banks/<int:pk>/', Bankdetails.as_view(),name='single_bank'),
    path('users/', Userlist.as_view(),name='users'),
    path('users/<int:pk>/',Userdetails.as_view(),name='single_user')
   
]
