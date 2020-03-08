import socket

sk = socket.socket(type=socket.SOCK_DGRAM)# udp协议


name = input('请输入您的名字:')
# 收发
while 1:
    msg_s = input(('>>>'))
    info = name + ' : ' + msg_s
    sk.sendto(info.encode('utf-8'), ('127.0.0.1',8090))  # 发给谁的消息
    msg_r,addr = sk.recvfrom(1024)# 接收来自于哪里的消息
    print(msg_r.decode('utf-8'))


sk.close()