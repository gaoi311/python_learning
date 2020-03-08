"""
今日面试题：

def extend_list(v, li=[]):
    li.append(v)
    return li

list1 = extend_list(10)
print(list1)  # [10, ]
list2 = extend_list(123, [])
list3 = extend_list('a')

print(list1)  # [10, a]
print(list2)  # [123]
print(list3)  # [10, a]

print(list1 is list3)

# 第二题：问以下代码的输出结果是什么？
list1 = ["a", "b", "c", "d", "e"]
print(list1[10:])

# 第三题：如何打乱一个有序的列表？
"""

# list1 = ["a", "b", "c", "d", "e"]
# print(list1[10:])  # []
# print(list1[1:])  # ["b", "c", "d", "e"]
# print(list1[1:0])  # []

# print(list1[1::2])  # "b", "c", "d", "e"

# list2 = reversed(list1)
# print(list(list2))
# print(list1)
# print(list1[::-1])  # 利用切片翻转列表，生成一个新列表不是操作的原来的列表
# print(list1)

# 直接操作原来列表的方法
# list1 = [11, 22, 33]
# append()
# list1.append([44, 55])
# print(list1)
# # remove()
# list1.remove(33)
# print(list1)
# # extend()
# list1.extend([44, 55])
# print(list1)
# list1.insert(0, 0)
# print(list1)

# 1求学要严谨
# list1.insert(9, 99)
# print(list1)

# list1.pop(0)  # 返回被弹出的那个元素
# print(list1)
# list1.pop(9)  # IndexError: pop index out of range
# print(list1)

# list1.reverse()  # 反转原来的列表
# print(list1)

# list1.clear()  # 清空原列表
# print(list1)


# 第三题：如何打乱一个有序的列表？
# list1 = [11, 22, 33, 44, 55]
# import random
# random.shuffle(list1)
# print(list1)
#
#
# # 常量
# PI = 3.1415926


list1 = [11, 22, 33, 44]
ret = "+".join([str(x) for x in list1])
print(ret)

# Python三元运算
a = 100
b = 200
# 如果a的值大于b，就把a的值赋值给c,否则把b的值赋值给c
if a > b:
    c = a
else:
    c = b

c = a if a > b else b

