from django.urls import path
from . import views
from rest_framework.authtoken.views import(
obtain_auth_token)

urlpatterns = [
  
    path('', views.pyclient1, name = "pyclient1"),
    path('product/', views.pyclient2, name = "pyclient2"),
    path('drf/product/', views.pyclient3, name = "pyclient3"),
    path('drf/product/create/', views.product_create_view, name = "pyclient4"),
    path('drf/product/update/<int:pk>', views.product_update_view, name = "pyclient5"),
	path('drf/product/delete/<int:pk>', views.product_del_view, name = "pyclient6"),
	path('drf/products/list/', views.product_list_view, name = "pyclient7"),
	path('drf/auth/', obtain_auth_token, name = "py-auth"),

]
