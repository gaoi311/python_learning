from concurrent.futures import ProcessPoolExecutor
import requests

def func(num):
    sum = 0
    for i in range(num):
        sum += i ** 2
    return sum

def call_back_fun(res):
    print(res.result())

if __name__ == '__main__':

    t = ProcessPoolExecutor(20)

    for i in range(1000):
        t.submit(func, i).add_done_callback(call_back_fun)
    t.shutdown()