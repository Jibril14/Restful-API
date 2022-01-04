from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import json
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


