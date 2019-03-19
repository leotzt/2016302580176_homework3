from socket import *

host = ''
port = 3000
buffersize = 2048
address = (host,port)

ss = socket(AF_INET,SOCK_STREAM)
ss.bind(address)
ss.listen(3)

while True:
    print('Connecting')
    ss_temp,address = ss.accept()
    print ("Connection from :",address)
    str = 'Message'
    while True:
        data = ss_temp.recv(buffersize)
        if not data:
            break
        ss_temp.send(('%s : %s' % (str,data)))
    ss_temp.close()
ss_temp.close()