# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json

host = sys.argv[1]
textport = sys.argv[2]

dictionary = {"name" : "John",
              "age" : 30,
              "city": "New York"}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

for x in range(10):
    s.sendto(json.dumps(dictionary).encode('utf-8'), server_address)
    dictionary["age"] += 1 

