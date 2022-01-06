
import requests


product_id = input("Enter a number:" )
try:
	product_id = int(product_id)
except:
	product_id = None
	print(f"{product_id} not a valid id")

if product_id:	
	endpoint = f"http://127.0.0.1:8000/api/drf/product/delete/{product_id}"
	response = requests.delete(endpoint,  json={"name":"Hi World"})

print(response) 
print(response.json())