import socket
import json

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()

conn,addr = sk.accept()


# 通信

str_dic = conn.recv(9090).decode('utf-8')
dic = json.loads(str_dic)
# dic = {'opt':menu.get(num),'filename':filename,'content':content}
if dic['opt'] == 'upload':
    # 上传
    filename = '1' + dic['filename']
    with open(filename,'w',encoding='utf-8') as f:
        f.write(dic['content'])



elif dic['opt'] == 'download':
    # 下载
    pass





conn.close()
sk.close()


