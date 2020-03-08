# 客户端发送要执行命令
# 服务器执行,执行完将结果返回给客户端
# 客户端拿到结果呈现到用户眼前

import socket

sk = socket.socket()

sk.connect_ex(('127.0.0.1',8080))
while 1:
    cmd = input('请输入一个命令>>>')
    sk.send(cmd.encode('utf-8'))

    result = sk.recv(102400).decode('gbk')

    print(result)


sk.close()















