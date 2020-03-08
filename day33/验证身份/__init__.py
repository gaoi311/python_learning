import hashlib

import hmac
import os

# print(os.urandom(16),len(os.urandom(16)))

sor = b'wusir'
r_str = os.urandom(16)

md5_obj = hmac.new(sor,r_str)
r = md5_obj.digest()

# md5_obj = hashlib.md5(sor)
# md5_obj.update(r_str.encode('utf-8'))
# r = md5_obj.hexdigest()

print(r)
b'\xab\xf2\xa28\xf6\xc0\xe7\x86\xf2\xb6\xb6oCN\x05\xc1'
b'r\xf6\xbd\xa0E\x88T\x95\xc4\x8a\xc6\xc3\xff1\x10_'