# 计算器 周末作业

# collections模块
# 数据类型的扩展模块

# 什么是队列
# 先进先出
# import queue
# q = queue.Queue()
# print(q.qsize())
# q.put(1)
# q.put('a')
# q.put((1,2,3))
# q.put(({'k':'v'}))
# print(q.qsize())
# print('q : ',q)
# print('get : ',q.get())
# print(q.qsize())

# deque 双端队列
# from collections import deque
# dq = deque()
# dq.append(2)
# dq.append(5)
# dq.appendleft('a')
# dq.appendleft('b')
# print(dq)
# # print(dq.pop())
# # print(dq)
# # print(dq.popleft())
# # print(dq)
# print(dq.remove('a'))
# print(dq.insert(2,'123'))
# print(dq)

# 总结
# 在insert remove的时候 deque的平均效率要高于列表
# 列表根据索引查看某个值的效率要高于deque
# append 和pop对于列表的效率是没有影响






