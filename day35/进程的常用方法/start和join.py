from multiprocessing import Process
import time

def func():
    for i in range(500):
        time.sleep(0.01)
        print('儿子在这里')

if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    p.join()# 是让主进程等待子进程执行完。  现象：主进程执行到这句话，主进程阻塞住，等待子进程执行
    # time.sleep(1)
    for i in range(100):
        time.sleep(0.01)
        print('爸爸在这里')

# 开启一个正常的子进程，父进程会等待子进程结束后，父进程也就是程序才结束
# p.join()# 是让主进程等待子进程执行完。  现象：主进程执行到这句话，主进程阻塞住，等待子进程执行
# 如何把父进程和子进程之间的关系变为同步或者异步？
# 父进程执行join，就会变成同步，不执行join，父进程和子进程就是异步的关系
# join必须放在start()后边