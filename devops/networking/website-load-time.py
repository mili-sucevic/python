import time
from urllib.request import urlopen

start_time = time.time()

# Open the website and read the response
response = urlopen("http://www.example.com")
html = response.read()

end_time = time.time()

# Calculate the total loading time
total_time = end_time - start_time

print("Website loading time: ", total_time, " seconds")
