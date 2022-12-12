import requests

# Send a request to a web service that returns your IP address
response = requests.get("http://ip.42.pl/raw")

# Print the response, which is your IP address
print("Your IP address is: ", response.text)
