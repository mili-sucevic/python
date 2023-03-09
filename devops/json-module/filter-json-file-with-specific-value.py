import json

def filter_json_file(file, key, value):
    with open(file, "r") as f:
        data = json.load(f)
    
    filtered_data = [item for item in data if item[key] == value]
    
    print(json.dumps(filtered_data, indent=4))

filter_json_file("data.json", "age", 32)
