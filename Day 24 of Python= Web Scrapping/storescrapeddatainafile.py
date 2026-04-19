import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

with open("data.txt", "w") as file:
    for p in soup.find_all("p"):
        file.write(p.text + "\n")