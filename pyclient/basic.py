import requests


# Making request to a web page
endpoint = "https://www.github.com/"
endpoint = "http://127.0.0.1:8000/"
response = requests.get(endpoint)

print(response) # returns a response object <Response[200]>
print(dir(response)) # returns different response type available
print(response.text) # print raw html text response in unicode
print(response.status_code) # return a success status code 200
print(response.ok) # returns True for status code less than 400
print(response.headers) # returns headers info such as the server,
# 'Content-Type': 'text/html', Cross-Origin etc



# Making request to a web API

endpoint = "http://httpbin.org/get?page=15&count=8/" # Passing url parameter directly
payload = {"page": 15, "count":8}
response = requests.get(endpoint, params = payload) # params args = a dictionary of url parammeterss

print("response txt",response.text) # print out JSON object
print("Response url",response.url) #  http://httpbin.org/get?page=15&count=8/&page=15&count=8
print("response json",response.json()) # Like doing json.load since response is json, .json() returns a python dict(null value become None)



# Making a POST request to a web API

endpoint = "https://httpbin.org/post" 
payload = {"Name": "Abdullahi", "message":" I'm a boy"}
response = requests.post(endpoint, data = payload) # form data args = a dictionary of data 

print(response.text) # returns a Json, with form data = username & password
print(response.json()) # Now a python dict
print(response.json()['form']) # Access form key & print it value

##################################

endpoint = "https://httpbin.org/post" 
response = requests.post(endpoint, json={"query":"Hello World"}) # json args = a dictionary of data. would not accept data here 

print(response.text) # returns a Json, 
print(response.json()) # Now a python dict
print(response.json()['json']) # Access json key & print it value {"query":"Hello World"}



# Passing Auth Credencials to a web API

auth = ( "Abdullahi", "test1234")  
endpoint = "http://httpbin.org/basic-auth/Abdullahi/test1234"  # Passing data to url directly or

response = requests.get(endpoint, auth = auth) # auth args = a tupple 
print(response.text) # returns a Json, {"authenticated":true}
print(response) # status <Response[200]>

response = requests.get("http://httpbin.org/basic-auth/Abdullahi/test1234", auth = ("Abdulliii", "test1234")) # passong wrong username
print(response.text) # No response
print(response) # Return status response code 401



# Timing Response to a web API

response = requests.get("http://httpbin.org/basic-auth/Abdullahi/test1234", auth = ("Abdullahi", "test1234"), timeout=1) # After 1s if no response then terminate(ReadTimeout exceptions)
print("res",response)

response = requests.get("http://httpbin.org/delay/5", timeout=3) # Must terminate due to timeout 3s & 5s delay (ReadTimeout exceptions)
print(response)

