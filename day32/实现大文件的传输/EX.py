
# import os
# filesize = os.path.getsize('__init__.py')
#
#
# with open('__init__.py','rb') as f:
#     while filesize:
#         content = f.read(1024)
#         sk.send(content)
#         filesize -= len(content)


import struct

a = 2140000000
# -21E<a<21E

# s = struct.pack('i',a)
# print(s,len(s))
# print(struct.unpack('i',s))
# send(dic_len + dic)   --- > recv(4)

# print(b'123' + b'456')
import os
print(os.listdir('/'))
