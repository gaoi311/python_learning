# import socket
# import time
# sk = socket.socket()
#
# sk.connect(('192.168.12.104',18080))# 连接
#
# time.sleep(20)
#
# sk.close()



#    第二次      通信
import socket
import time
sk = socket.socket()

sk.connect(('192.168.12.104',18080))# 连接

sk.send('中文'.encode('utf-8'))

sk.close()