import socket

sk = socket.socket()# 默认参数  使用基于网络类型的套接字,TCP协议
sk.bind(('127.0.0.1',65534))# 回环地址
sk.listen()
while 1:
    conn,addr = sk.accept()# 接电话

    while 1:
        msg_r = conn.recv(1024).decode('utf-8')
        print(msg_r)
        if msg_r == 'q':
            break
        msg_s = input('>>>')
        conn.send(msg_s.encode('utf-8'))
        if msg_s == 'q':
            break

    conn.close()
sk.close()