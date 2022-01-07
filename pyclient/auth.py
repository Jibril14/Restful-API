import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/drf/auth/"

username = input("Enter your username\n" )
password = getpass("Enter your password\n" )

auth_response = requests.post(auth_endpoint,  json={"username": username, "password": password})

print(auth_response) 
print(auth_response.json())

if auth_response.status_code == 200:
	token = auth_response.json()["token"] # grab token from auth_response
	headers = {
		"Authorization": f"Token {token}"
	}
	endpoint = "http://127.0.0.1:8000/api/drf/products/list/"
	response =  requests.get(endpoint,  headers=headers)
	print(response.json())
	print(response.headers)
