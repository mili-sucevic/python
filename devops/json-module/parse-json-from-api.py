import requests
import json

url = "https://api.example.com/data"
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    print(json.dumps(data, indent=4))
else:
    print("Failed to retrieve data from API.")
