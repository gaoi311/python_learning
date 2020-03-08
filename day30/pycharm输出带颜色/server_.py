import socket

sk = socket.socket(type=socket.SOCK_DGRAM)# udp协议
sk.bind(('127.0.0.1',8090))
# 需求: 根据每个客户端的名字,去加上颜色
dic = {'alex':'\033[32m','金老板':'\033[33m','晓雪':'\033[35m'}

# 收发
while 1:
    msg_r,addr = sk.recvfrom(1024)# 接收来自于哪里的消息
    # 消息     alex : 我是SB
    msg_r = msg_r.decode('utf-8')
    name = msg_r.split(':')[0].strip()
    color = dic.get(name,'')# get(key,default)  获取字典中key对应的value,如果没有key则返回default
    print('%s %s \033[0m'%(color,msg_r))
    msg_s = input(('>>>'))
    sk.sendto(msg_s.encode('utf-8'),addr)# 发给谁的消息

sk.close()