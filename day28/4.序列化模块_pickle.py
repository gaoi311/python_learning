# pickle
dic = {1:(12,3,4),('a','b'):4}
import  pickle

# dump的结果是bytes,dump用的f文件句柄需要以wb的形式打开,load所用的f是'rb'模式
# 支持几乎所有对象的序列化
# 对于对象的序列化需要这个对象对应的类在内存中
# 对于多次dump/load的操作做了良好的处理

# pic_dic = pickle.dumps(dic)
# print(pic_dic)    # bytes类型
# new_dic = pickle.loads(pic_dic)
# print(new_dic)

# pickle支持几乎所有对象的
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# alex = Student('alex',83)
# ret = pickle.dumps(alex)
# 小花 = pickle.loads(ret)
# print(小花.name)
# print(小花.age)

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# alex = Student('alex',83)
# with open('pickle_demo','wb') as f:
#     pickle.dump(alex,f)
# with open('pickle_demo','rb') as f:
#     旺财 = pickle.load(f)
#     print(旺财.name)

# 学员选课系统  pickle模块来存储每个学员的对象

# with open('pickle_demo','wb') as f:
#     pickle.dump({'k1':'v1'}, f)
#     pickle.dump({'k11':'v1'}, f)
#     pickle.dump({'k11':'v1'}, f)
#     pickle.dump({'k12':[1,2,3]}, f)
#     pickle.dump(['k1','v1','l1'], f)

# with open('pickle_demo','rb') as f:
#     while True:
#         try:
#             print(pickle.load(f))
#         except EOFError:
#             break

