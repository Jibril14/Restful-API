import requests

endpoint = "http://127.0.0.1:8000/api/drf/product/mixin/list"
response = requests.get(endpoint) # list all products

print(response) 
print(response.json())


endpoint = "http://127.0.0.1:8000/api/drf/product/mixin/detail/2"
response = requests.get(endpoint)  # get a product detail

print(response) 
print(response.json())



endpoint = "http://127.0.0.1:8000/api/drf/product/mixin/create"
data = {"name":"Tecno  pro", "price":300}
response = requests.post(endpoint, json=data)  # create a product 

print(response) 
print(response.json())