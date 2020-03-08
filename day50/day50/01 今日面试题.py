"""
一个楼梯有50个台阶，每一步可以走一个台阶，也可以走两个台阶，请问走完这个楼梯共有多少种方法？
"""

# ret = f(n)

# 1. 不管怎么走， 最后要么剩一个台阶，要么剩两个台阶
# 最后剩一个台阶：f(n-1)
# 最后剩两个台阶：f(n-2)

# f(1) =                1
# f(2) =                2
# f(3) = f(1) + f(2)    3
# f(4) = f(2) + f(3)    5
# f(5) = f(3) + f(4)    8
# f(6) = f(4) + f(5)    13


def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f(n-1) + f(n-2)


def func(num):
    n, a, b = 0, 0, 1
    yield b
    while n < num:
        a, b = b, a + b
        yield b
        n = n + 1


g = func(4)
for i in range(5):
    print("第" + str(i) + "个值：", g.__next__())

# 汉诺塔游戏如何用Python代码表示

