import socket
sk = socket.socket()
sk.connect(('127.0.0.1',8080))

msg_s = input('>>>')
sk.send(msg_s.encode('utf-8'))

print(sk.recv(1024).decode('utf-8'))

sk.close()