import requests


endpoint = "http://127.0.0.1:8000/api/products/delete/4"


response = requests.delete(endpoint)

print(response.status_code)