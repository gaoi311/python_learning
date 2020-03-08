
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)

while 1:
    sk.sendto(b'hello',('127.0.0.1',8888))
    sk.sendto(b'world',('127.0.0.1',8888))

sk.close()