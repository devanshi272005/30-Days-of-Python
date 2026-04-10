import json

data = {
    "name": "Devanshi",
    "age": 20,
    "marks": 95
}

# Write JSON
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Read JSON
with open("data.json", "r") as file:
    data = json.load(file)
    print(data["name"])