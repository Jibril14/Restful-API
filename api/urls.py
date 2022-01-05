from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.pyclient1, name = "pyclient1"),
    path('product/', views.pyclient2, name = "pyclient2"),
    path('drf/product/', views.pyclient3, name = "pyclient3"),
]
