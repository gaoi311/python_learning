from gevent import monkey
monkey.patch_all()
import gevent
import time

def func1(num):
    time.sleep(1)
    print(num)

start = time.time()
for i in range(10):
    func1(i)
print(time.time() - start)


start = time.time()
l = []
for i in range(10):
    g = gevent.spawn(func1,i)
    l.append(g)
gevent.joinall(l)
print(time.time() - start)
