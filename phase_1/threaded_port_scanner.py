import socket
import time
import threading 

min_port_range = 20
max_port_range = 80

domains = [
    "scanme.nmap.org",
    "portquiz.net",
]

def do_scan(host, port):
    s = socket.socket()  # creates a socket object
    s.connect_ex((host, port))
    valid = s.connect_ex((host, port)) # attempts to connect, 0 if valid
    s.close() # always close a socket after use

    if valid == 0:
        print("[HOST] " + host + " has an open port of: " + str(port))
    else:
        print("[HOST] " + host + " has a closed port of: " + str(port))

def scan_port(host):
    threads = []
    start_time = time.time()

    for port in range(min_port_range, max_port_range):
        t = threading.Thread(target=do_scan, args=(host, port))
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join() # wait for each thread

    print("Scan took: " + str(time.time() - start_time))

scan_port("portquiz.net")