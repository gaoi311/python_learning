# 类方法

# class A:
#     def func(self):  # 普通方法
#         print(self)
#
#     @classmethod  # 类方法
#     def func1(cls):
#         print(cls)


# a1 = A()

# a1.func()
# A.func(a1)


# 类方法: 通过类名调用的方法,类方法中第一个参数约定俗称cls,python自动将类名(类空间)传给cls.
# A.func1()

# a1 = A()
# a1.func1()  # 对象调用类方法,cls 得到的是类本身.


#类方法的应用场景:
#1, 类中 有些方法是不需要对象参与.

# class A1:
#     name = 'alex'
#     count = 1
#
#     @classmethod
#     def func1(cls):  # 此方法无需对象参与
#         return cls.name + str(cls.count + 1)

# A.func1(111) 不可取
# a1 = A()
# print(a1.func1())
# print(A.func1())


# 静态方法

# 2, 对类中的静态变量进行改变,要用类方法.

# 3,继承中,父类得到子类的类空间.

class A:
    age = 12
    @classmethod
    def func1(cls):  # 此方法无需对象参与
        # print(cls)
        # 对B类的所有的内容可以进行修改.
        cls.age = 20
        print(cls.age)
        # return cls.name + str(cls.count + 1)

class B(A):
    age = 22
B.func1()

# 不通过类方法,想让我的父类的某个方法得到子类的类空间里面的任意值.
# class A:
#     age = 12
#
#     def func2(self):
#         print(self)  # self 子类的对象,能得到子类 空间的任意值
#
# class B(A):
#     age = 22
#
# b1 = B()
# b1.func2()

# 静态方法:
class A:

    @staticmethod
    def login(username, password):
        if username == 'alex' and password == 123:
            print('登录成功')
        else:
            print('登录失败...')


A.login('alex',1234)

# def login(username,password):
#     if username == 'alex' and password == 123:
#         print('登录成功')
#     else:
#         print('登录失败...')
#
# login('alex',1234)

# 1,代码块.清晰.
# 2,复用性.
