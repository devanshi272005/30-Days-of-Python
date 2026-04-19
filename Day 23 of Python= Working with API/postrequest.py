import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Python API",
    "body": "Learning APIs",
    "userId": 1
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())