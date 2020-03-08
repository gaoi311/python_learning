from multiprocessing import Queue

q = Queue(3)

q.put(1)
q.put('abc')
q.put([4,5,6])
# print(123)
# q.put('汉子')
# try:
#     q.put_nowait('汉子')
# except:
#     print('队列满了')
# print(456)

print(q.get())
print(q.get())
print(q.get())
# print(q.get())# 阻塞等待
try:
    print(q.get_nowait())
except:
    print('队列空了')