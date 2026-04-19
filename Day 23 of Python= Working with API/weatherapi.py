import requests

api_key = "YOUR_API_KEY"
city = input("Enter city: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

print("Temperature:", data["main"]["temp"])
print("Weather:", data["weather"][0]["description"])