import time

def func():
    print(123)
    sum = 0
    print(6666)
    yield sum
    print(7777)
    yield sum
    print(8888)
    yield sum

def fff():
    g = func()
    print('这是在ffff函数中')
    print(next(g))
    time.sleep(1)
    print('这是在ffff函数中')
    print(next(g))
    time.sleep(1)
    print('这是在ffff函数中')
    print(next(g))

fff()


# g = func()# 并不会执行func函数
# print('abc')
# time.sleep(10)
# print(next(g))
# time.sleep(10)
# fff()
# time.sleep(10)
# print(next(g))