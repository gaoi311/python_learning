#     第一次
# import socket
# import time
# sk = socket.socket()# 不传参数,默认使用基于网络类型的套接字, 协议 : TCP
#
# sk.bind(('192.168.12.104',18080))# 端口的范围是0-65535   但是 0-1023 这些你别用
# sk.listen()# 同时能接受的连接
#
# print(123)
# conn,addr = sk.accept()# 等待接受客户端的连接  阻塞等待
# print(456)
# print('conn:',conn)
# print('addr:',type(addr))
#
# time.sleep(20)
#
# conn.close()
# sk.close()


#    第二次   通信

import socket
import time
sk = socket.socket()# 我买一个新手机

sk.bind(('192.168.12.104',18080))#  我买一个手机卡

sk.listen()# 开机

print(123)
conn,addr = sk.accept()# 等待朋友给我打电话


msg_r = conn.recv(10)# 接受数据,接受10个字节
print(msg_r.decode('utf-8'),addr)


conn.close()# 挂断电话
sk.close() # 关机


