import json

def is_valid_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True

data = '{"name": "John Doe", "age": 32, "email": "johndoe@example.com"}'

if is_valid_json(data):
    print("Valid JSON data.")
else:
    print("Invalid JSON data.")
