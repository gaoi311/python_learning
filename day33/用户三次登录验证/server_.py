import socketserver
import json
import hashlib

def zhuce():
    pass

class MySocket(socketserver.BaseRequestHandler):
    def handle(self):
        sor = b'wusir'#
        while 1:
            str_dic = self.request.recv(1024).decode('utf-8')
            # 接收到 一个字典，类似于{'status':False,'username':None,'password':None}
            if not str_dic:break # 当客户端登录失败退出程序的情况下，这里会接收到一个空消息。
            dic = json.loads(str_dic)
            if not dic['status']:
                '''没有登录成功的情况下'''
                with open('info','r',encoding='utf-8') as f:
                    # 文件内容的存储方式  用户名|密码
                    for info in f:
                        username,pawd_txt = info.strip().split('|')
                        if username == dic['username']:
                            '''用户存在，就对客户端发来的用户的密码再次加密，与文件中对比'''
                            md5_obj = hashlib.md5(sor)
                            md5_obj.update(dic['password'].encode('utf-8'))
                            pawd = md5_obj.hexdigest()
                            if pawd_txt == pawd:
                                '''密码正确的情况下'''
                                dic['status'] = True
                            else:
                                dic['reason'] = '密码错误'
                            break
                    else:
                        '''用户不存在'''
                        dic['reason'] = '用户不存在'
                        zhuce()
                #  dic = {status:False ,  username ,   password,   reason}
                #  dic = {status:True ,  username ,   password}
                str_dic = json.dumps(dic)
                self.request.send(str_dic.encode('utf-8'))
            else:
                '''已经是登录成功了'''

server = socketserver.TCPServer(('127.0.0.1',8080),MySocket)
server.serve_forever()


