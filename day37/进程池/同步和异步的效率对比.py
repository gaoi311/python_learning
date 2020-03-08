from multiprocessing import Pool
import requests
import time

def func(url):
    res = requests.get(url)
    print(res.text)
    if res.status_code == 200:
        return 'ok'

if __name__ == '__main__':
    p = Pool(5)
    l = ['https://www.baidu.com',
         'http://www.jd.com',
         'http://www.taobao.com',
         'http://www.mi.com',
         'http://www.cnblogs.com',
         'https://www.bilibili.com',
         ]
    start = time.time()
    for i in l:
        p.apply(func,args=(i,))

    apply_= time.time() - start

    start = time.time()
    for i in l:
        p.apply_async(func, args=(i,))
    p.close()
    p.join()
    print('同步的时间是%s，异步的时间是%s'%(apply_, time.time() - start))
