import json

def update_json_file(file, data):
    with open(file, "r") as f:
        json_data = json.load(f)
    
    json_data.update(data)
    
    with open(file, "w") as f:
        json.dump(json_data, f, indent=4)

update_json_file("data.json", {"new_key": "new_value"})
