# from multiprocessing import Queue# 是用于多进程的队列，就是专门用来做进程间通信（IPC）。
# import queue# 是用于同一进程内的队列，不能做多进程之间的通信

# q = queue.Queue()
# # 先进先出
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())

# q = queue.LifoQueue()
# # 后进先出的队列
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())

# q = queue.PriorityQueue()
# 优先级队列，put()方法接收的是一个元组（），第一个位置是优先级，第二个位置是数据
# 优先级如果是数字，直接比较数值
# 如果是字符串，是按照 ASCII 码比较的。当ASCII码相同时，会按照先进先出的原则
# q.put((1,'abc'))
# q.put((5,'qwe'))
# q.put((-5,'zxc'))
# print(q.get())
# print(q.get())
# print(chr(48))

###########################################################

# from multiprocessing import Queue
# import queue
#
# q = queue.Queue()
#
# q.put(1)
# q.put(2)
#
# print(q.get())
# print(q.get())



from multiprocessing import Queue
import queue

q = queue.PriorityQueue()

q.put((3, 'abc'))
q.put((2, 'qwe'))
q.put((1, 'zxc'))
print(q.get())
print(q.get())
print(q.get())