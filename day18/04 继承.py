# encoding:utf-8
# 面向对象的三大特性: 继承 多态 封装

# 继承

# class Animal:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age

# class Person:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
# class Cat:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
# class Dog:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
# p1 = Person('alex','laddyboy',1000)

# class Animal:
#     breath = '呼吸'
#
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print(self)
#         print('动物都需要进食....')
#
#
# class Person(Animal):  # 括号里面的 父类,基类,超类   括号外面的 子类,派生类.
#     pass
#
#
# class Cat:
#     pass
#
#
# class Dog:
#     pass
#
#
# p1 = Person('alex', 'laddyboy', 1000)
# print(p1.__dict__)

# 初识继承:
# 子类以及子类实例化的对象 可以访问父类的任何方法或变量.
# 类名可以访问父类所有内容
# print(Person.breath)
# Person.eat(111)
# 子类实例化的对象也可以访问父类所有内容
# print(p1.breath)
# print(p1)
# p1.eat()

# 查询顺序 (看截图)


#  写三个类: 狗,猫,鸡, 每个类中都有 吃 喝  自己的方法  最后定义一个Animal类,

# class Animal:
#
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self,a1):
#         print('%s吃%s' % (self.name,a1))
#
#     def drink(self):
#         print('%s喝东西' % (self.name))
#
#
# class Cat(Animal):
#
#     def miaow(self):
#         print('喵喵叫')
#     # def eat(self):  # 只执行自己类中的方法
#     #     print(666)
#
# class Brid(Animal):
#
#     def __init__(self, name,sex,age,wing): # self b1对象 name '鹦鹉',sex '公',age 20,  wing '绿翅膀'
#         '''
#         self=b1对象
#         name='鹦鹉'
#         sex='公'
#         age= 20,
#         wing='绿翅膀'
#         '''
#         # Animal.__init__(self, name, sex, age)
#         super().__init__(name,sex,age)  #  super(Brid,self).__init__(name,sex,age)
#         self.wing = wing
#     def bark (self):
#         print('嗷嗷叫')
#
#     def eat(self,argv):
#         super().eat(argv)
#         print('鸟吃虫子...')
#
# class Chook(Animal):
#     def crow(self):
#         print('大爷laiwanya')
# # cat1 = Cat('tom','公', 3)
# # # cat1.eat()
# # 只执行父类的方法:子类中不要定义与父类同名的方法
# # 只执行子类的方法:在子类创建这个方法.
# # 既要执行子类的方法,又要执行父类的方法?
# # 有两种解决方法.
#     # 1,Animal.__init__(self, name, sex, age)
#     # 1,super().__init__(name,sex,age)
# # cat1 = Cat('tom','公', 3,)
#
# b1 = Brid('鹦鹉','公',20,'绿翅膀')
# # print(b1.__dict__)
# b1.eat('金蝉')
# def func1(a1,a2):
#     print(a1)
#     print(a2)
#
# def func2(argv1,argv2,argv3):
#     print(argv1)
#     func1(argv2,argv3)
#
# func2(1,2,3)

# 继承的进阶
# 继承: 单继承,多继承.


# 类: 经典类, 新式类
# 新式类: 凡是继承object类都是新式类.
    # python3x 所有的类都是新式类,因为python3x中的类都默认继承object.
# class A:
#     pass
# 经典类: 不继承object类都是经典类
    #python2x:(既有新式类,又有经典类) 所有的类默认都不继承object类,所有的类默认都是经典类.你可以让其继承object.

# 单继承: 新式类,经典类查询顺序一样.

# class A:
#     pass
#     # def func(self):
#     #     print('IN A')
#
# class B(A):
#     pass
#     # def func(self):
#     #     print('IN B')
#
# class C(B):
#     pass
#     # def func(self):
#     #     print('IN C')
#
# c1 = C()
# c1.func()

# 多继承:
    #  新式类: 遵循广度优先.
    #  经典类: 遵循深度优先.

# 多继承的新式类  广度优先 : 一条路走到倒数第二级,判断,如果其他路能走到终点,则返回走另一条路.如果不能,则走到终点.

# class A:
#     def func(self):
#         print('IN A')
#
# class B(A):
#     pass
#     # def func(self):
#     #     print('IN B')
#
# class C(A):
#     pass
#     # def func(self):
#     #     print('IN C')
#
# class D(B):
#     pass
#     # def func(self):
#     #     print('IN D')
#
# class E(C):
#     pass
#     # def func(self):
#     #     print('IN E')
#
# class F(D,E):
#     pass
#     # def func(self):
#     #     print('IN F')
#
# f1 = F()
# f1.func()


# class A:
#     def func(self):
#         print('IN A')
#
# class B(A):
#     pass
#     # def func(self):
#     #     print('IN B')
#
# class C(A):
#     pass
#     # def func(self):
#     #     print('IN C')
#
# class D(B):
#     pass
#     # def func(self):
#     #     print('IN D')
#
# class E(C):
#     def func(self):
#         print('IN E')
#
# class F(D,E):
#     pass
#     # def func(self):
#     #     print('IN F')
#
# f1 = F()
# f1.func()
#
# print(F.mro())  # 查询类的继承顺序


# 多继承的经典类  深度优先 : 一条路走到底.
# print 111

# class A:
#     pass
#     # def func(self):
#     #     print('IN A')
# 
# class B(A):
#     pass
#     # def func(self):
#     #     print('IN B')
# 
# class C(A):
#     # pass
#     def func(self):
#         print('IN C')
# 
# class D(B):
#     pass
#     # def func(self):
#     #     print('IN D')
# 
# class E(C):
#     # pass
#     def func(self):
#         print('IN E')
# 
# class F(D,E):
#     pass
#     # def func(self):
#     #     print('IN F')
# 
# f1 = F()
# f1.func()