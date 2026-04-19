import requests
from bs4 import BeautifulSoup

html = """
<div class="item"><h2>Item1</h2><p>100</p></div>
<div class="item"><h2>Item2</h2><p>200</p></div>
"""

soup = BeautifulSoup(html, "html.parser")

items = soup.find_all("div", class_="item")

for item in items:
    name = item.find("h2").text
    price = item.find("p").text
    print(name, price)