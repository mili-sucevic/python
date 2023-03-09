import json

def sort_json_file(file, key):
    with open(file, "r") as f:
        data = json.load(f)
    
    data = sorted(data, key=lambda k: k[key])
    
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

sort_json_file("data.json", "age")
