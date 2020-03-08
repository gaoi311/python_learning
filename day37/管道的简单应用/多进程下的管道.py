from multiprocessing import Pipe,Process

def func(con):
    con1,con2 = con
    con1.close()# 子进程使用con2和父进程通信，所以
    while 1:
        try:
            print(con2.recv())#当主进程的con1发数据时，子进程要死循环的去接收。
        except EOFError:# 如果主进程的con1发完数据并关闭con1，子进程的con2继续接收时，就会报错，使用try的方式，获取错误
            con2.close()# 获取到错误，就是指子进程已经把管道中所有数据都接收完了，所以用这种方式去关闭管道
            break

if __name__ == '__main__':
    con1,con2 = Pipe()
    p = Process(target=func,args=((con1,con2),))
    p.start()
    con2.close()# 在父进程中，使用con1去和子进程通信，所以不需要con2，就提前关闭
    for i in range(10):# 生产数据
        con1.send(i)# 给子进程的con2发送数据
    con1.close()# 生产完数据，关闭父进程这一端的管道
















