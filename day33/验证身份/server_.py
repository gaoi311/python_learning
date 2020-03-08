# import socket
# import hashlib
# sk = socket.socket()
# sk.bind(('127.0.0.1',8080))
# sk.listen()
#
# conn,addr = sk.accept()
# sor = b'alex'
# r_str = '这是一个随机的字符串'
# conn.send(r_str.encode('utf-8'))
#
# md5_obj = hashlib.md5(sor)
# md5_obj.update(r_str.encode('utf-8'))
# result = md5_obj.hexdigest()
#
# msg = conn.recv(1024).decode('utf-8')
# if msg == result:
#     conn.send(b'success')
# else:
#     conn.send(b'failed')
#
#
# conn.close()
# sk.close()



########################################简单的优化
'''优化的地方：
上述代码中，随机的字符串是固定的，不是真正随机的
在这里用os.urandom(num) 随机出一个num位的随机bytes

加密算法上述代码直接使用的是hashlib，
在这里简便成，使用hmac这个新模块中的new方法，去进行加密
md5_obj = hmac.new(盐，随机字符串)
r = md5_obj.digest()
拿到一个bytes的结果，也就是密文
'''

import socket
import hashlib
import os
import hmac
sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()

conn,addr = sk.accept()
sor = b'alex'
r_str = os.urandom(16)# 随机出一个16位长度的bytes
conn.send(r_str)

md5_obj = hmac.new(sor,r_str)
result = md5_obj.digest()


msg = conn.recv(1024)
if msg == result:
    conn.send(b'success')
else:
    conn.send(b'failed')


conn.close()
sk.close()