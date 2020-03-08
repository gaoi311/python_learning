# hash方法
# 底层数据结构基于hash值寻址的优化操作
# hash是一个算法
# 能够把某一个要存在内存里的值通过一系列计算,
# 保证不同值的hash结果是不一样的
# '127647862861596'  ==> 927189778748
# 对同一个值在多次执行python代码的时候hash值是不同
# 但是对同一个值 在同一次执行python代码的时候hash值永远不变
# print(hash('abc'))  # 6048279107854451739
# print(hash('abc'))
# print(hash('abc'))
# print(hash('abc'))
# print(hash('abc'))
# print(hash('abc'))

# 字典的寻址  - hash算法
# d = {'key':'value'}
# hash - 内置函数

# set集合
# se = {1,2,2,3,4,5,'a','b','d','f'}
# print(se)

# d = {'key':'v1','key':'v2'}
# print(d['key'])

# hash(obj) #obj内部必须实现了__hash__方法






