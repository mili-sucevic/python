import speedtest

st = speedtest.Speedtest()

# Print the results of the speed test
download = st.download()
upload = st.upload()
ping = st.results.ping

print("Download speed: ", download, " Mbps")
print("Upload speed: ", upload, " Mbps")
print("Ping: ", ping, " ms")
