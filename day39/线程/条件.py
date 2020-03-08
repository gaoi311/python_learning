from threading import Condition,Thread
import time




def func(con,i):
    con.acquire()# 主线程和10个子线程都在抢夺递归锁的一把钥匙。
    # 如果主线程抢到钥匙，主线程执行while 1，input，然后notify发信号，还钥匙。但是，此时如果主线程执行特别快
    # 极有可能接下来主线程又会拿到钥匙，那么此时哪怕其他10个子线程的wait接收到信号，但是因为没有拿到钥匙，所以其他子线程还是不会执行
    con.wait()
    print('第%s个线程执行了'%i)
    con.release()

con = Condition()
for i in range(10):
    t = Thread(target=func,args = (con,i))
    t.start()
while 1:
    # print(123)
    con.acquire()
    num = input('>>>')
    con.notify(int(num))
    con.release()
    time.sleep(0.5)

# 条件 涉及 4个方法：
#    con.acquire()
#    con.release()
#    con.wait()  # 假设有一个初始状态为False，阻塞。一旦接受到notify的信号后，变为True，不再阻塞
#    con.notify(int)  给wait发信号，发int个信号，会传递给int个wait，让int个线程正常执行