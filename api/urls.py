from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.pyclient1, name = "pyclient1"),
]
