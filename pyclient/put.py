import requests

endpoint = "http://127.0.0.1:8000/api/drf/product/update/2"
response = requests.put(endpoint,  json={"name":"Hi World"})

print(response) 
print(response.json())