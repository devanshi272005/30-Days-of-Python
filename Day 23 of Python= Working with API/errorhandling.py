import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url)
    response.raise_for_status()
    print("Success")
except requests.exceptions.RequestException as e:
    print("Error:", e)