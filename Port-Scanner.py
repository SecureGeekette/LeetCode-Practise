""" Write a port scanner similar to nmap (Network Map) which is an application that performs network discovery
 and identifies open, closed and filtered ports on hosts and determines device type & OS """

# If a packet is sent to a closed TCP port, we generally get a TCP reset (RST) - if port is unfitered
# If a packet is sent to a closed UDP port, we get ICMP destination unreachable - if port is unfiltered
# If port is filtered, we generally get no response

# socket is used for network connections
# sys is used for command line arguments

import socket, sys
target = sys.argv[1]
ports = range(1,9001)

for port in ports:

    try:
        # A new socket object sock is created using IPv4 address family and TCP protocol STREAM
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # This is an attempt to establish a TCP connection to the target on the current port
        if sock.connect_ex((target, port)) == 0:
            print("The port ", port, " is open")
        #else:
            #print("The port ", port, " is closed")

    except socket.error:
        print("Error with socket")


