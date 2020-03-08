"""
问:执行完下面的代码后,  l,m的内容分别是什么?
"""
import copy


# def func(m):
#     for k, v in m.items():
#         m[k+2] = v+2
#
#
# m = {1: 2, 3: 4}
#
# l = m l和m指向了同一块内存地址  # copy.copy()浅拷贝, copy.deepcopy()  l = {1:2， 3:4}
#
# l[9] = 10  # l: {1:2, 3:4, 9:10}
#
# func(l)  # l: {1:2, 3:4, 5:6, 9:10, 11:12}
#
# m[7] = 8  # {1:2, 3:4, 7:8}

# l: {3:4, 5:6, 11:12}
# m: {}

# list1 = [11, 22, 33, 44]
# for i in list1:
#     list1.append("a")


# 引申补充
# 回去复习下：
# 1. 小数据池
# 2. 深浅拷贝的概念和用法


# list1 = [11, 22, 33, 44]
# list2 = list1[::]  # 类似于深copy
# list1[0] = 10
# print(list1)
# print(list2)

print(round(6.5))