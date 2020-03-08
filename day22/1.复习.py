# class Saler:
#     def __init__(self,name,sex,ident):
#         self.name = name
#         self.sex = sex
#         self.ident = ident
#     def sale(self):
#         print('%s卖东西'%self.name)
#     def add_goods(self):
#         pass
# alex = Saler('alex',None,'looser')
# print(type(alex))
# print(type(Saler))  # Saler类 -> Saler类型 类型的类型 = 类型

# class Consumer:
#     pass

# from abc import ABCMeta
# class A(metaclass=ABCMeta):pass
# print(type(A))

# 面向对象
#     你写代码的时候 什么时候用面向对象
#         代码量大,功能多的时候
#         处理比较复杂的角色之间的关系
#             qq 好友 陌生人 群 组
#             复杂的电商程序
#             公司/学校的人事管理/功能的系统
#         我的代码的清晰度更高了
#             可读性 无论是开发者 还是调用者 都能明确的分辨出每个角色拥有的方法和属性
#             增强了代码可扩展性
#             增加复用性
#             更加规范
#     python当中一切皆对象 基础数据类型 都是对象
#     类型和自定义类的关系  类型和类是一个东西
#         type(obj) obj是一个对象,那么它的type就是它的类型
#     创建一个对象
#         类名() 实例化
#         __new__()创造了一个对象的空间,一些简单的初始化
#     创建一个类
#         class 类名 语法级别的 python解释器读到这句话的时候
#         type是所有类的元类,object是所有类的父类
#         类也是被创建出来的,type创建类, type(cls) = type
#         class A(metaclass=ABCMeta) ABCMeta创建了这个A类,那么ABCMeta就是A的元类
#         那么 type就是这个类的 元类
#     type(obj) 的结果就是这个对象所属的类
#     type(类)的结过就是创建这个类的元类,大多数情况下就是type,除非你指定metaclass

# 类 class Leiming
    # 类是什么时候被加载的,以及类名是什么时候生效的
    # 类
        # 静态属性/静态字段/静态变量
        # 动态属性/方法
# class Person:
#     ROLE = 'CHINA'
#     # print(Person.ROLE)  # 报错
#     print(ROLE)
#     def func(self):
#         pass
# a = Person()
# print(Person.func)
# print(a.func)

# 对象
    # 类创造对象的过程就是实例化的过程 : 构造new,初始化init
    # 可以通过指针找到类的空间中的内容
    # 对象本身内部存储了一些只属于对象的属性
# 组合 什么有什么的关系
    # 一个类的对象作为另一个类对象的属性
# 继承 什么是什么的关系,节省代码
    # 子类 和 父类
    # 单继承 和 多继承
        # 单继承
            # 如果子类的对象调用某个方法
                # 子类有 : 调用子类的
                    # 子类有但想调父类的 :
                        # super : 不用自己传self super(子类,self).方法名(除了self之外的参数)
                        # 父类名: 父类名.方法名(self,...)
                # 子类没有 : 找父类
            #注意 在任何类中调用的方法,都要自习分辨一下这个self到低是谁的对象
# class Foo:
#     def __init__(self):
#         self.func()
#
#     def func(self):print('Foo.func')
#
# class Son(Foo):
#     def func(self):print('Son.func')
# s = Son()
    # 多继承
        # 新式类 : 广度优先 - C3算法
            # mro方法查看继承顺序
            # py3 默认继承object  所以py3都是新式类
                # super().func() 遵循mro算法,在类的内部不用传子类名和self
            # py2 需要主动继承object
                # super(子类名,self).func() 必须传子类名和self
        # 经典类 : 深度优先
            # py2 不继承object,默认都是经典类
            # 没有mro
# class A:
#     def func(self):
#         print('A')
#
# class B(A):
#     def func(self):
#         super().func()
#         print('B')
#
# class C(A):
#     def func(self):
#         super().func()
#         print('C')
#
# class D(B,C):
#     def func(self):
#         super().func()
#         print('D')
# d = D()
# d.func()
# b= B()
# b.func()

    # 抽象类和接口类
    #     不能被实例化
    #     规范子类当中必须实现某个方法
    #     有原生的实现抽象类的方法,但是没有原生实现接口类的方法
    #
    #     抽象类 : 抽象类中的方法是可以实现的 只能单继承
    #     接口类 : 可以多继承 但是这个类中的所有方法都不应该实现
    # java
        # java 只支持类的单继承 抽象类  父类的方法可以实现
        # 接口 interface 支持多继承的规范 接口中的所有方法 只能写pass
# Interface 会飞的动物
    # fly
# 会走的动物
    # walk
# 会游泳的动物
    # swim
#  老虎(会走的动物,会游泳的动物)
    # walk
    # swim
# 青蛙(会走的动物,会游泳的动物)
    # walk
    # 游泳
# 天鹅(会走的动物,会游泳的动物,会飞的动物)
    # walk
    # 游泳
    # 飞

# 多态 在python当中处处存在
    # 一种类型的多种形态  多个子类去继承父类,那么每一个子类都是这个父类的一种形态
# class Animal:pass
# class Tiger(Animal):pass
# class Frog(Animal):pass
    # java中多态应用
# java
# def func(Animal laohu_or_frog):
#     laohu_or_frog.eat()

# python
# def func(obj):
#     obj.eat()

    # 鸭子类型 规范全凭自觉

# 封装  私有的
    # 广义的封装 : 把方法和属性都封装在一个类里,定义一个规范来描述一类事物.
    # 狭义的封装 : 私有化 只能在类的内部访问
    # __静态变量,私有方法   ,私有的对象属性,私有的类方法,私有的静态方法
    # 在内存中存储 _类名__名字
    # 为什么在类的内部可以使用双下划线访问 : 在类的内部使用,你就知道你在哪个类中
    # 在子类中可以访问访问父类的私有变量么?不行
    # 私有 : 不能在类的外部使用也不能被继承

# property 装饰器函数,内置函数,帮助你将类中的方法伪装成属性,特性
    # 调用方法的时候不需要主动加括号
    # 让程序的逻辑性更合理
    # @方法名.setter  装饰器,修改被property装饰的属性的时候会调用被这个装饰器装饰的方法,除了self之外还有一个参数,被修改的值
    # @方法名.deleter 装饰器,当要删除被property装饰的属性的时候会调用被这个装饰器装饰的方法

# 只用property
# class Circle:
#     def __init__(self,r):
#         self.r = r
#         # self.area = 3.14*self.r**2
#
#     @property
#     def area(self):   #  这个方法计算结果本身就是是一个属性,但是这个属性会随着这个类/对象的一些基础变量的变化而变化
#         return 3.14*self.r**2

# c = Circle(5)
# print(c.area)
# c.r = 10
# print(c.area)

# 偏其他语言 property+私有的 合用 ,这个时候更多的也会用到setter和deleter
# class A:
#     def __init__(self,name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,new_name):
#         if type(new_name) is str:
#             self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
# a = A('alex')
# a.name = 123
# print(a.name)
# del a.name   # 语法
# print(a.name)

# classmethod 类方法的装饰器 内置函数
# 使用类名调用,默认传类名作为第一个参数
# 不用对象命名空间中的内容,而用到了类命名空间中的变量(静态属性),或者类方法或静态方法
# class Goods:
#     __discount = 0.8
#     def __init__(self,price):
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price * Goods.__discount
#     @classmethod
#     def change_discount(cls,num):
#         cls.__discount = num
#
# # 商场的程序
# apple = Goods(10)
# banana = Goods(15)
# print(apple.price,banana.price)
# Goods.change_discount(1)
# print(apple.price,banana.price)

# staticmethod 静态方法的装饰器 内置函数
# 如果一个类里面的方法 既不需要用到self中的资源,也不用cls中的资源.
# 相当于一个普通的函数
# 但是你由于某种原因,还要把这个方法放在类中,这个时候,就将这个方法变成一个静态方法
# 某种原因:
    # 你完全想用面向对象编程 ,所有的函数都必须写到类里
    # 某个功能确确实实是这个类的方法,但是确确实实没有用到和这个类有关系的资源

# 学生 管理员
# 课程 班级
# class Person:
#     @staticmethod
#     def login():  # 动词 动作 属于某一个对象
#         pass
# class Student(Person):pass
# class Manager(Person):pass
# class Course:pass
# class Classes:pass

# object.__new__()

# 反射 - 从某个指定的命名空间中,用字符串数据类型的变量名来获取变量的值
# 类名反射 静态属性 类方法 静态方法
# 对象反射 对象属性 方法
# 模块     模块中的方法
# 自己模块中
# import sys
# mymodule = sys.modules['__main__']
# getattr(mymodule,'变量名')

# hasattr/getattr/setattr/delattr
# 参数
    # (命名空间,'变量名')
    # setattr(命名空间,'变量名',新的值)
# 变量名 你只能拿到一个字符串的版本
    # 从文件里拿
    # 交互拿 :input / 网络传输

# a = '你好'
# print(a.encode('utf-8'))

# 进阶
    # 内置方法/魔术方法/双下方法
    # __名字__不是被直接调用的
    # 间接调用 : 内置函数/面向对象中特殊语法/python提供的语法糖
    # __str__ : str(obj),要求必须实现了__str__,要求这个方法的返回值必须是字符串str类型
        # print %s str
    # __call__  : 对象()  用类写装饰器
    # __len__ : len(obj),要求obj必须实现了__len__,要求这个方法的返回值必须是数字int类型
    # __new__ : 在实例化的过程中,最先执行的方法,在执行init之前,用来创造一个对象,构造方法
        # 单例类
    # __init__  : 在实例化的过程中,在new执行之后,自动触发的一个初始化方法

# x  = 5
# y = 6
# print(x.__add__(y))
# print(x+y)   # 语法糖

# class MyType:
#     def __init__(self,s):
#         self.s = s
#
#     def __add__(self, other):   # __sub__ __mul__ __div__
#         return self.s.count('*') + other.s.count('*')
#
# obj1 = MyType('asjkfhk***17264****')
# obj2 = MyType('asjkfhk***17***')
# print(obj1 + obj2)
# print(obj1.__add__(obj2))
# print('ashglhg**uowqeyo88'.count('*'))

# 'sfi1974974*****729359' + 'sfi1974974*****729359'
