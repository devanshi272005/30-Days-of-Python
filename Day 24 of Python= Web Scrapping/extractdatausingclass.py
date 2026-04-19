import requests
from bs4 import BeautifulSoup

html = """<div class="product">
<h2>Phone</h2>
<p>Price: 20000</p>
</div>"""

soup = BeautifulSoup(html, "html.parser")

product = soup.find("div", class_="product")

print(product.find("h2").text)
print(product.find("p").text)