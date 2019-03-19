from socket import *

host ='localhost'
port = 3000
buffersize=2048
address = (host,port)
ss = socket(AF_INET,SOCK_STREAM)
ss.connect(address)

while True:
    data = raw_input()
    if not data:
        break
    ss.send(data)
    data = ss.recv(buffersize)
    if not data:
        break
    print data
ss.close()