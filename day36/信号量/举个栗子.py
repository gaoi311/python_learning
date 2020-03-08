from multiprocessing import Semaphore,Lock

# l = Lock()
# l.acquire()
# print(123)
# l.acquire()
# print(456)


# l = Semaphore(4)
#
# l.acquire()# 拿走1把钥匙，锁上门
# print(123)
# l.acquire()# 拿走1把钥匙，锁上门
# print(456)
# l.acquire()# 拿走1把钥匙，锁上门
# print(789)
# # l.release()
# l.acquire()# 拿走1把钥匙，锁上门
# print(120)