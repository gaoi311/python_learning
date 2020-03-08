


import json
import hashlib

sor = b'wusir'
u = 'xiaoxue'
p = 'pangpangde'

md5_obj = hashlib.md5(p.encode('utf-8'))
md5_obj.update(u.encode('utf-8'))
r = md5_obj.hexdigest()

md5_obj = hashlib.md5(sor)
md5_obj.update(r.encode('utf-8'))
res = md5_obj.hexdigest()
print(res)


