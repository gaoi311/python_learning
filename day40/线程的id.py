from threading import Thread
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor
import time
def func(i):
    sum = 0
    sum += i
    time.sleep(1)
    print('这是在子线程中',current_thread())
    return sum

def call_back(sum):
    time.sleep(1)
    print('这是在回调函数中',sum.result(),current_thread())


if __name__ == '__main__':
    t = ThreadPoolExecutor(5)
    for i in range(10):
        t.submit(func,i).add_done_callback(call_back)
    t.shutdown()
    print('这是在主线程中',current_thread())











# def func():
#     print(current_thread())
#
#
# Thread(target=func).start()
# print(current_thread())