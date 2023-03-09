import json

def print_json_value(file, key):
    with open(file, "r") as f:
        data = json.load(f)
    
    print(data.get(key))

print_json_value("data.json", "name")
