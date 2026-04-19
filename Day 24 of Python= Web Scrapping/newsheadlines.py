import requests
from bs4 import BeautifulSoup

url = "https://example.com"   # replace with news site
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

for h in soup.find_all("h2"):
    print(h.text)