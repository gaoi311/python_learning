# __名字__
    # 类中的特殊方法\内置方法
    # 双下方法
    # 魔术方法   magic_method
# 类中的每一个双下方法都有它自己的特殊意义

# __call__ 相当于 对象()
# __len__  len(obj)
# __new__  特别重要   开辟内存空间的 类的构造方法
    # 写一个单例类=
# __str__  str(obj),'%s'%obj,print(obj)

# 所有的双下方法 没有 需要你在外部直接调用的
# 而是总有一些其他的 内置函数 特殊的语法 来自动触发这些 双下方法

# __call__ flask
# class A:
#     def __call__(self, *args, **kwargs):
#         print('执行call方法了')
#     def call(self):
#         print('执行call方法了')
# class B:
#     def __init__(self,cls):
#         print('在实例化A之前做一些事情')
#         self.a = cls()
#         self.a()
#         print('在实例化A之后做一些事情')
# a = A()
# a()  # 对象() == 相当于调用__call__方法
# a.call()

# A()() # 类名()() ,相当于先实例化得到一个对象,再对对象(),==>和上面的结果一样,相当于调用__call__方法
# B(A)

# __len__
# 内置函数和类的内置方法是由奸情的
# len(dict)
# len(tuple) str list set
# class mylist:
#     def __init__(self):
#         self.lst = [1,2,3,4,5,6]
#         self.name = 'alex'
#         self.age = 83
#     def __len__(self):
#         print('执行__len__了')
#         return len(self.__dict__)
#
# l = mylist()
# print(len(l))
# len(obj)相当于调用了这个obj的__len__方法
# __len__方法return的值就是len函数的返回值
# 如果一个obj对象没有__len__方法,那么len函数会报错

# iter和next的例子
# __iter__  iter(obj)
# __next__  next
# def iter(obj):
#     return obj.__iter__()
# l = [1,2,3]
# iter(l) # l.__iter__()

# 练习
# 类
# self.s = ''
# len(obj) = str的长度
# class My:
#     def __init__(self,s):
#         self.s = s
#     def __len__(self):
#         return len(self.s)
# my = My('abc')
# print(len(my))

# __new__    # ==> 构造方法
# __init__  # ==> 初始化方法

# class Single:
    # def __new__(cls, *args, **kwargs):
    #     # print('在new方法里')
    #     obj = object.__new__(cls)
    #     print('在new方法里',obj)
    #     return obj

    # def __init__(self):
    #     print('在init方法里',self)

# 1.开辟一个空间,属于对象的
# 2.把对象的空间传给self,执行init
# 3.将这个对象的空间返回给调用者
# obj = Single()
# single的new,single没有,只能调用object的new方法
# new方法在什么时候执行???
    # 在实例化之后,__init__之前先执行new来创建一块空间

# 单例
# 如果一个类 从头到尾只能有一个实例,说明从头到尾之开辟了一块儿属于对象的空间,那么这个类就是一个单例类
# class A:pass
# a = A()
# a2 = A()
# a3 = A()
# print(a,a2,a3)

# 单例类
class Single:
    __ISINCTANCE = None
    def __new__(cls, *args, **kwargs):
        if not cls.__ISINCTANCE:
            cls.__ISINCTANCE = object.__new__(cls)
        return cls.__ISINCTANCE
    def __init__(self,name,age):
        # self.name = name
        # self.age = age
        print(self)

s1 = Single('alex',83)
s2 = Single('taibai',40)
# print(s1.name)
# print(s2.name)
# print(s1,s2)

# __str__
# l = [1,2,3]  # 实例化一个list的对象
# # l是个对象
# print(l)

class Student:
    def __str__(self):
        return '%s %s %s'%(self.school,self.cls,self.name)

    def __init__(self,name,stu_cls):
        self.school = 'oldboy'
        self.name = name
        self.cls = stu_cls

he = Student('hezewei','py14')
print(he)
# huang = Student('huangdongyang','py14')
# print(huang)
# print(str(he))   # 内置的数据类型,内置的类,相当于执行__str__
print('学生1 : %s'%he)

# print一个对象相当于调用一个对象的__str__方法
# str(obj),相当于执行obj.__str__方法
# '%s'%obj,相当于执行obj.__str__方法




