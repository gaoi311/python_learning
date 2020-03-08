import socket
import time
# from socket import SOL_SOCKET,SO_REUSEADDR
sk = socket.socket()
# sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sk.setblocking(False)# 设置accept和recv两个方法的阻塞与非阻塞状态
# 参数为False   代表设置为非阻塞状态
# 参数为True 或者不写，默认为阻塞状态
sk.bind(('127.0.0.1',8080))
# sk.settimeout(4)# 设置等待超时时间
# print(sk.gettimeout())# 获取等待超时时间
sk.listen()
# print(123)
time.sleep(1)
conn,addr = sk.accept()# 阻塞
# print(456)
print(conn.recv(1024))# 阻塞
# print(789)
# print(conn.recv(1024))
# print(conn.getpeername())# 获取连接的远端的地址
# print(conn.getsockopt())

conn.close()
sk.close()
