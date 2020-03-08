import socket
import time
sk = socket.socket()
while 1:
    r = sk.connect_ex(('127.0.0.1',8080))
    if r == 0:
        break

time.sleep(5)

sk.send(b'hello')
# print(sk.getsockname())# 获取当前套接字的地址


# sk.sendall(b'world')

sk.close()