import requests

try:
    response = requests.get("https://example.com")
    response.raise_for_status()
    print("Success")
except requests.exceptions.RequestException as e:
    print("Error:", e)