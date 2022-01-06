from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from product.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializers import ProductSerializer

from rest_framework import generics

def pyclient1(request, *args, **kwargs):

	#Getting info  from client
	# Requesting for headers of response

	data = {}
	print(request.GET) # django request return query params by default
	print(request.POST) # return posted data 
	data["params"] = dict(request.GET) # <QueryDict: {'username': ['Abdullahi']}>
	data["headers"] = dict(request.headers)
	#data["headers"] = request.headers
	data["content_type"] = request.content_type
	#print(data) # returns a bite string of json data 
	return JsonResponse(data) # returning json 


def pyclient2(request, *args, **kwargs):
	# Returning data from Product models to client
	product_data = Product.objects.all().order_by("?").first()
	data = {} # turn to dict
	if product_data:
		data = model_to_dict(product_data, fields=["id", "name"]) # Narrow down data
		#data["id"] = product_data.id
		#data["name"] = product_data.name
		#data["description"] = product_data.description
		#data["price"] = product_data.price

	return JsonResponse(data) # returning json to client


# python request to DRF view
@api_view(["GET"])
def pyclient3(request, *args, **kwargs):
	# Returning data from Product models to client
	product = Product.objects.all().order_by("?").first()
	data = {} # turn to dict
	if product:
		data = ProductSerializer(product).data

	return Response(data) # returning json to client


class ProductCreateAPIView(generics.CreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def perform_create(self, serializer):
 		name = serializer.validated_data.get("name")
 		description = serializer.validated_data.get("description")
 		
 		if description is None:
 			description = name
 		serializer.save(description=description)

product_create_view = ProductCreateAPIView.as_view()
 	 

 
 # cbv put method
class ProductUpdateAPIView(generics.UpdateAPIView):
 	queryset = Product.objects.all()
 	serializer_class = ProductSerializer
 	#lookup_field = 'pk'

 	def perform_update(self, serializer):
 		instance = serializer.save()
 		if not instance.description:
 			instance.description = instance.name

product_update_view = ProductUpdateAPIView.as_view()



 # cbv destroy method
class ProductDeleteAPIView(generics.DestroyAPIView):
 	queryset = Product.objects.all()
 	serializer_class = ProductSerializer
 	#lookup_field = 'pk'

 	def perform_destroy(self, instance):
 		super().perform_destroy(instance)
 		

product_del_view = ProductDeleteAPIView.as_view()

