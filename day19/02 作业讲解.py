#
# day17天作业及默写
# 一，简答题：
#
# 1，面向对象的三大特性是什么？
#     继承 多态 封装.
#
# 2，什么是面向对象的新式类？什么是经典类？
#
# 3，面向对象为什么要有继承？继承的好处是什么？
#             优化代码,节省代码.
#             提高代码的复用性.
#             提高代码的维护性.
#             让类与类之间发生关系.
# 4，面向对象的广度优先，深度优先分别是什么？
#
# 5，面向对象中super的作用。
#     在子类中调用父类的方法.
#
# 二，代码题(通过具体代码完成下列要求)：
# 1，
# a,定义一个父类Animal，在构造方法中封装三个属性，姓名，性别，年龄，
# 再给其添加一个eat的方法，方法中显示%s正在吃饭（%s是哪个对象调用此方法，显示哪个对象名字）。
# b,定义两个子类Person,Dog，全部继承这个父类Animal.
# c,Person类中，有构造方法，封装一个皮肤的属性，有eat方法，方法中显示人类正在吃饭。
# d,Dog类中，有构造方法，封装一个毛色的属性，有eat方法，方法中显示狗狗正在吃饭。
# 上面这几个类创建完成之后，完成下列要求：
# ①：	实例化一个人类的对象，让其只封装皮肤属性。
# ②： 实例化一个人类的对象，让其封装姓名，性别，年龄，皮肤四个属性。
# ③： 实例化一个狗类的对象，让其只封装毛色属性。
# ④： 实例化一个狗类的对象，让其封装姓名，性别，年龄，毛色四个属性。
# ⑤： 实例化一个人类的对象，让其只执行父类的eat方法（可以对人类代码进行修改）。
# ⑥： 实例化一个狗类的对象，让其既执行父类的eat方法，又执行子类的eat方法。

# class Animal:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def eat(self):
#         print('%s 在吃东西' % self.name)
#
# class Person(Animal):
#     def __init__(self,name,sex,age,skin):
#         super().__init__(name,sex,age)
#         self.skin = skin
#     def eat(self):
#         print('人类正在吃饭')
#
# class Dog(Animal):
#     def __init__(self,coat_colour):
#         self.coat_colour = coat_colour
#     def eat(self):
#
#         print('狗狗正在吃饭')
# p1 = Person('李富贵','男',18,'黄皮肤')
# print(p1.__dict__)

#
#
#
#
#
# 2，
# class E:
#     def func(self):
#         print('in E')
#
# class A(E):
#
#     def func(self):
#         print('in A')
#
# class B:
#     def func(self):
#         print('in B')
#
# class C(A,B):
#     def func(self):
#         super(A,self).func()
#         print('in C')
# 可以改动上上面代码，完成下列需求：
# 对C类实例化一个对象产生一个c1，然后c1.func()
# c1 = C()
# c1.func()
# 1, 让其执行C类中的func
# 2，让其执行A类中的func

# 3，让其执行B类中的func

# 4，让其既执行C类中的func，又执行A类中的func

# 5，让让其既执行C类中的func，又执行B类中的func
#
# 3，下面代码执行结果是什么？为什么？
# class Parent:
#     def func(self):
#         print('in Parent func')
#
#     def __init__(self):
#         self.func()
#
# class Son(Parent):
#     def func(self):
#         print('in Son func')
#
# son1 = Son()
#
# 4，
# class A:
#     name = []
#
# p1 = A()
# p2 = A()
# p1.name.append(1)

# p1.age = 12
# p1.name，p2.name，A.name 分别又是什么？为什么？
# print(p1.age)
# print(p2.age)
# print(A.age)
# p1.name，p2.name，A.name 分别是什么？
# print(p1.name)
# print(p2.name)
# print(A.name)

# name = 'alex'
# name1 = []

#
class A:
    name = 'alex'

# p1 = A()
# p2 = A()
# p1.name = 'wusir'
# print(p1.name)
# print(A.name)


class A:
    pass
    # def func(self):
    #     print('IN A')

class B(A):
    pass
    # def func(self):
    #     print('IN B')

class C(A):
    # pass
    def func(self):
        print('IN C')

class D(B):
    pass
    # def func(self):
    #     print('IN D')

class E(C):
    # pass
    def func(self):
        print('IN E')

class F(D,E,B):
    pass
    # def func(self):
    #     print('IN F')

# f1 = F()
# f1.func()
print(F.mro())