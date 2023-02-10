import json
import csv

def convert_json_to_csv(json_file, csv_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for item in data:
            writer.writerow(item)

convert_json_to_csv("data.json", "data.csv")
