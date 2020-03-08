from multiprocessing import Pool
import requests
import time

def func(num):
    time.sleep(0.5)
    print(num+1)

if __name__ == '__main__':
    p = Pool(5)
    for i in range(100):
        p.apply_async(func, args=(i,))
        # time.sleep(0.5)
    p.close()
    p.join()
