import socket
sk = socket.socket()

sk.bind(('127.0.0.1',8888))
sk.listen()

conn,addr = sk.accept()

conn.send(b'hello')
conn.send(b'world')

conn.close()
sk.close()

