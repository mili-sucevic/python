# Test Internet Speed with Python

#import the necessary module
import speedtest 

st = speedtest.Speedtest()

option = int(input('''What speed do you want to test:  
  
1) Download Speed  
  
2) Upload Speed  
  
3) Ping 
  
Your Choice: '''))

#fetch the download speed
if option == 1:
  download = st.download()
  #converting into mbps
  download = download/1000000
  print(f"Your Download speed is", round(download, 3), "Mbps")

#fetch the upload speed 
elif option == 2:
  upload = st.upload()
  #converting into mbps
  upload = upload/1000000
  print("Your Upload speed is", round(upload, 3), "Mbps")
  
#fetch the ping
elif option == 3:
  servernames =[]  
  st.get_servers(servernames)  
  print(st.results.ping)  
  
else:
  print("Please enter the correct choice! :P") 
