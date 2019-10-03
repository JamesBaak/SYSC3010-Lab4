# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

# args = textport N
textport = sys.argv[1]
n = sys.argv[2]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

for i in range(int(n)):
    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)
    buf, address = s.recvfrom(port)
    if not len(buf):
        break
    print ("Received int %i from %s %s: " % (int(buf), address, buf ))

