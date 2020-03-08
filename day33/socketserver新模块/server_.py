import socketserver


class MySocket(socketserver.BaseRequestHandler):
    def handle(self):# 这个方法的名字是固定的，必须是这个名字
        # 收发的逻辑代码
        # self.request == conn
        msg = self.request.recv(1024).decode('utf-8')
        print(msg)
        self.request.send(msg.upper().encode('utf-8'))



server = socketserver.TCPServer(('127.0.0.1',8080),MySocket)# 固定的
server.serve_forever()# 开启一个永久性的服务



















