# def func(*args, **kwargs):
# args = (1,2,3)
# print(*args)  # print(*(1,2,3))
# print(**kwargs)  # print(**{'name':'alex', 'age':1000})

# 当定义一个函数的时候:* 代表 聚合.
# 当执行一个函数的时候:* 代表 打散.
# func(1, 2, 3, name='alex', age=1000)


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# func(*l1,*l2)
# func(*l1)
# print(1,2,3)


# def func1():
#     a = 1
#     b = 2
#     print(a)
#
#     def func2():
#         b = 3
#         print(b)
#
#     print(666)
#     func2()
#     print(111)
#
#
# func1()
# 1  666 3 111


# def func1():
#     a = 1
#     b = 2
#     print(a)
#
#     def func2():
#         b = 3
#         print(b)
#
#     print(666)
#     return func2
#
#
# func1()()

# l1 = [i for i in range(1,100)]
# l1 = [i for i in range(1,100) if i > 50]
# l1 = [i for i in range(1,100) if i > 50]