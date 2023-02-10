import json

json_data = '{"name": "John Doe", "age": 32, "email": "johndoe@example.com"}'

data = json.loads(json_data)
print(data)
