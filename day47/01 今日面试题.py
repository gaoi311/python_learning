"""
# 编写代码实现func函数，使其实现以下效果：
foo = func(8)

print(foo(8))  # 输出64
print(foo(-1))  # 输出-8

课后思考：用两个栈实现消息队列的功能？
"""


# def func(arg1):
#     def inner(arg2):
#         return arg1 * arg2
#     return inner
#
#
# foo = func(8)
# print(foo(8))
# print(foo(-1))

# -------------------------
def func(arg1):
    return lambda x:x*arg1


foo = func(8)
print(foo(8))
print(foo(-1))




