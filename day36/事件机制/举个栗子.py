from multiprocessing import Event

e = Event()
# e.set()
# e.clear()
# e.wait()
# e.is_set()
# 事件是通过is_set()的bool值，去标识e.wait() 的阻塞状态
# 当is_set()的bool值为False时，e.wait()是阻塞状态
# 当is_set()的bool值为True时，e.wait()是非阻塞状态
# 当使用set()时，是把is_set的bool变为True
# 当使用clear()时，是把is_set的bool变为False

print(e.is_set())# False wait应该是阻塞住
e.set()# 将is_set 的bool值变为True，将wait变为非阻塞
e.wait()
print(e.is_set())
print(123)
e.clear()
print(e.is_set())
e.wait()
print(123)


