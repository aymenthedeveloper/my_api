import requests


endpoint = "http://127.0.0.1:8000/api/products/create/"

data = {
    'title': 'hello world devs',
    'content': '',
    "price": 29.99
}

response = requests.post(endpoint, json=data)

print(response.json())