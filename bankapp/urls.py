from django.urls import path
from .views import *

urlpatterns = [
    path('users/', Userlist.as_view()),
    path('users/<int:pk>/',Userdetails.as_view())
   
]
