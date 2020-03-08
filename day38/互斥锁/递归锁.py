from threading import RLock

s = RLock()
s1 = RLock()
s.acquire()
s.acquire()
s.acquire()
s.acquire()
s.acquire()
s.acquire()
print(123)
