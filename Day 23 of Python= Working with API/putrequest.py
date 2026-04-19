import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {
    "title": "Updated Title",
    "body": "Updated Content",
    "userId": 1
}

response = requests.put(url, json=payload)

print(response.json())