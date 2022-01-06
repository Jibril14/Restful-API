import requests

endpoint = "http://127.0.0.1:8000/api/drf/product/create/"

response = requests.post(endpoint,  json={"name":"Oppo 5"})

print(response) 
print(response.json())