# Get IP Address of any website using python

#Import the necessary packages!
import socket as s 

#get hostname
my_hostname = s.gethostname()
#display my hostname
print(f"Your Hostname is: {my_hostname}")

#get IP
my_ip = s.gethostbyname(my_hostname)
#display IP 
print(f"Your Ip Address is: {my_ip}")

#set the hostname
host = 'google.com'
#fetch the IP
ip = s.gethostbyname(host)

#display the IP
print(f"The IP Address of {host} is {ip}")
