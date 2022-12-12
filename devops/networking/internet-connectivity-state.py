import urllib.request

# check for Internet connectivity
try:
    urllib.request.urlopen("http://google.com", timeout=1)
    print("Internet connectivity is present.")
    exit_status = 0
except urllib.request.URLError:
    print("Internet connectivity is not present.")
    exit_status = 1

# if there is a loss of connectivity, determine the cause and report it
if exit_status == 1:
    # check if DNS is not resolving
    try:
        urllib.request.urlopen("http://google.com", timeout=1)
    except urllib.request.URLError as err:
        if "Name or service not known" in str(err):
            print("The cause of the loss of connectivity is DNS not resolving.")
            print("A possible fix is to check the DNS settings and ensure that the DNS server is reachable.")

    # check if there is a connection timeout
    try:
        urllib.request.urlopen("http://google.com", timeout=1)
    except urllib.request.URLError as err:
        if "timed out" in str(err):
            print("The cause of the loss of connectivity is a connection timeout.")
            print("A possible fix is to check the network settings and ensure that the connection is stable.")

# set the exit status
exit(exit_status)

