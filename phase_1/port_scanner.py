# use a with statement
# add timeout
# return more readable data other than "None"
#

import socket

def do_scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates a socket object

    if s.connect_ex((host, port)) == 0: # port is open
        try:
            banner = s.recv(1024)
        finally:
            s.close()
            return banner
    else:
        s.close()

print("Started")

b1 = do_scan("scanme.nmap.org", 21) # FTP
b2 = do_scan("scanme.nmap.org", 22) # SSH
b3 = do_scan("scanme.nmap.org", 80) # HTTP

print(b1)
print(b2)
print(b3)

print("Finished")