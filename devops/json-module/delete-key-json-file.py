import json

def delete_json_key(file, key):
    with open(file, "r") as f:
        data = json.load(f)
    
    data.pop(key, None)
    
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

delete_json_key("data.json", "email")
