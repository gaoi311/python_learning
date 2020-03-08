# import socket
# import hashlib
# sk = socket.socket()
# sk.connect(('127.0.0.1',8080))
# sor = b'wusir'
# r_str = sk.recv(1024)
#
# md5_obj = hashlib.md5(sor)
# md5_obj.update(r_str)
# result = md5_obj.hexdigest()
# sk.send(result.encode('utf-8'))
#
# msg = sk.recv(1024)
# print(msg)
# sk.close()
################################优化




import socket
import hmac
sk = socket.socket()
sk.connect(('127.0.0.1',8080))
sor = b'alex'
r_str = sk.recv(1024)

md5_obj = hmac.new(sor,r_str)
result = md5_obj.digest()

sk.send(result)

msg = sk.recv(1024)
print(msg)










