import json

data = {
    "name": "John Doe",
    "age": 32,
    "email": "johndoe@example.com"
}

print(json.dumps(data, indent=4))
