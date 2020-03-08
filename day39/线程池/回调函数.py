from concurrent.futures import ProcessPoolExecutor
# 不管是ProcessPoolExecutor的进程池  还是Pool的进程池，回调函数都是父进程调用的。
import os
import requests



def func(num):
    sum = 0
    for i in range(num):
        sum += i ** 2
    return sum

def call_back_fun(res):
    # print(res.result(),os.getpid())
    print(os.getpid())

if __name__ == '__main__':
    print(os.getpid())
    t = ProcessPoolExecutor(20)
    for i in range(1000):
        t.submit(func,i).add_done_callback(call_back_fun)
    t.shutdown()
