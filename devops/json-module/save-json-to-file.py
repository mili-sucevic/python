import json

data = {
    "name": "John Doe",
    "age": 32,
    "email": "johndoe@example.com"
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data written to file successfully.")
