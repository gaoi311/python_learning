import time

# 在单线程中，如果存在多个函数，如果有某个函数发生IO操作，我想让程序马上切换到另一个函数去执行
#  以此来实现一个假的并发现象。
# 总结：
#    yield 只能实现单纯的切换函数和保存函数状态的功能
#    不能实现：当某一个函数遇到io阻塞时，自动的切换到另一个函数去执行
#    目标是：当某一个函数中遇到IO阻塞时，程序能自动的切换到另一个函数去执行
#            如果能实现这个功能，那么每个函数都是一个协程
#
#    但是  协程的本质还是主要依靠于yield去实现的。
#
#    如果只是拿yield去单纯的实现一个切换的现象，你会发现，跟本没有程序串行执行效率高

def consumer():
    while 1:
        x = yield
        # print(x)

def producer():
    g = consumer()
    next(g)
    for i in range(100000000):
        g.send(i)

start = time.time()
producer()
print('yield:',time.time() - start)








def consumer(l):
    # for i in l:
        # print(i)
    pass

def producer():
    l = []
    for i in range(100000000):
        l.append(i)
    return l

start = time.time()
l = producer()
consumer(l)
print(time.time() - start)