from django.urls import path
from app1.views import *
app_name='some1'

urlpatterns=[
    path('car/',car,name='car'),
]