from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from product.models import Product

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

 