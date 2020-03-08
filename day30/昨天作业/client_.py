import socket

sk = socket.socket()
sk.connect(('127.0.0.1',65534))
while 1:
    msg_s = input('>>>')
    sk.send(msg_s.encode('utf-8'))
    if msg_s == 'q':
        break
    msg_r = sk.recv(1024).decode('utf-8')
    if msg_r == 'q':
        break
    print(msg_r)

sk.close()