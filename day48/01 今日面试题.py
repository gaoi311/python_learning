"""
1. os和sys都是干什么的？
2. 你工作中都用过哪些内置模块？
3. 有没有用过functools模块？
"""
import os
# 1. os和sys都是干什么的？
# os模块是跟操作系统相关
# 拼接路径  Win:\  Unix: /   a\b   a/b
# os.path.join("a", "b")  # Django
# print(os.path.sep)   # 获取当前操作系统的路径分隔符
# print(os.sep)   # 获取当前操作系统的路径分隔符

# 获取文件的绝对路径  Django
# ret = os.path.abspath(__file__)
# print(ret)
# print(os.path.dirname(ret))

# 判断文件是否存在
# os.path.exists("文件的路径")
# 文件大小
# os.path.getsize("文件路径")
# 创建文件
# os.mkdir("文件路径")


# sys是合Python解释器相关
import sys
# sys.path
# sys.modules  # 获取Python解释器加载的所有模块
# sys.argv  # 获取脚本运行时的参数
# sys.exit()

# time/re/json/hashlib/random/socket/
# collection/functools
import functools
from functools import partial, reduce, wraps
# 命名元组
from collections import namedtuple


# 偏函数, 制定一个默认参数，包装成另外一个参数
# print(bin(10))
# print(oct(10))


print(int("10000", base=2))
print(int("1000", base=2))
print(int("100", base=2))
print(int("10", base=2))

int2 = partial(int, base=2)

print(int2("10000"))
print(int2("1000"))
print(int2("100"))
print(int2("10"))


