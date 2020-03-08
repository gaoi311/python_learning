# import socket
# #
# # sk = socket.socket(type=socket.SOCK_DGRAM)# udp协议
# #
# # sk.bind(('127.0.0.1',8090))
# #
# # # 收发
# # msg_r,addr = sk.recvfrom(1024)# 接收来自于哪里的消息
# # print(msg_r.decode('utf-8'))
# #
# # # sk.sendto()# 发给谁的消息
# #
# # sk.close()

# #＃＃＃＃＃＃＃＃＃＃＃＃＃聊天室程序　　一直收发
#
# import socket
#
# sk = socket.socket(type=socket.SOCK_DGRAM)# udp协议
# sk.bind(('127.0.0.1',8090))
#
# # 收发
# while 1:
#     msg_r,addr = sk.recvfrom(1024)# 接收来自于哪里的消息
#     print(msg_r.decode('utf-8'),addr)
#     msg_s = input(('>>>'))
#     sk.sendto(msg_s.encode('utf-8'),addr)# 发给谁的消息
#
# sk.close()








