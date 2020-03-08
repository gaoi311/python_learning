import socket
import os
import json

sk = socket.socket()
sk.connect_ex(('127.0.0.1',8080))# 带返回值,如果出错,不会报错,会返回错误的编码
# sk.connect()# 会直接报错    两个都是连接服务器的功能

menu = {'1':'upload','2':'download'}
for k,v in menu.items():
    print(k,v)

num = input('请输入功能选项:')

if num == '1':
    # 上传功能
    # {你要执行的功能, 文件名, 文件内容}
    dic = {'opt':menu.get(num),'filename':None,'content':None}
    file_path = input('请输入一个文件的绝对路径>>>')
    # D:/sylar/python_workspace/day31/文件上传下载/__init__.py
    filename = os.path.basename(file_path)
    with open(file_path,'r',encoding='utf-8') as f:
        content = f.read()

    dic['filename'] = filename
    dic['content'] = content
    # print(dic)
    str_dic = json.dumps(dic)
    sk.send(str_dic.encode('utf-8'))


# D:/sylar/python_workspace/day23/1.内容回顾.py

elif num == '2':
    # 下载功能
    pass
else:
    print('错误')





sk.close()