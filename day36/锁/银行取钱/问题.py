from multiprocessing import Process,Value,Lock
import time


def get_money(num,l):# 取钱
    l.acquire()# 拿走钥匙，锁上门，不允许其他人进屋
    for i in range(100):
        num.value -= 1
        print(num.value)
        time.sleep(0.01)
    l.release()# 还钥匙，打开门，允许其他人进屋

def put_money(num,l):# 存钱
    l.acquire()
    for i in range(100):
        num.value += 1
        print(num.value)
        time.sleep(0.01)
    l.release()

if __name__ == '__main__':
    num = Value('i',100)
    l = Lock()
    p = Process(target=get_money,args=(num,l))
    p.start()
    p1 = Process(target=put_money, args=(num,l))
    p1.start()
    p.join()
    p1.join()
    print(num.value)

# i = 35
# i += 1
#
# tmp = i
# tmp = tmp+1
# i = tmp













