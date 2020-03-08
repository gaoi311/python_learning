import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()
conn,addr = sk.accept()
while 1:
    msg = conn.recv(1024)
    print('wahaha')
    print(msg)
    if not msg:
        break




