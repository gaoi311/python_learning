import socket
sk = socket.socket(type=socket.SOCK_DGRAM)

sk.bind(('127.0.0.1',8888))
while 1:
    msg1 = sk.recvfrom(5)
    print('msg1:',msg1)

    msg2 = sk.recvfrom(1024)
    print('msg2:',msg2)

sk.close()