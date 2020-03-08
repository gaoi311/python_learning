import socket

sk = socket.socket(type=socket.SOCK_DGRAM)


while 1:
    msg_s = input('>>>')
    sk.sendto(msg_s.encode('utf-8'),('127.0.0.1',8090))
    msg_r,addr = sk.recvfrom(1024)
    print(msg_r.decode('utf-8'))

sk.close()

