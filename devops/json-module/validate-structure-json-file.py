import json

def validate_json_file(file):
    try:
        with open(file, "r") as f:
            data = json.load(f)
        print("The JSON file is valid.")
    except json.JSONDecodeError as e:
        print(f"The JSON file is invalid: {e}")

validate_
