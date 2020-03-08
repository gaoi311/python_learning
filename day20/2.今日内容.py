# 两个内置函数 *
# 反射  *****
# 内置方法 ***


# 类(定义)
    # 静态属性  类属性(变量)  直接写在类中,全大写
    # 动态属性  方法(函数)     self
    # 类方法    @classmethod   cls
    # 静态方法  @staticmethod  没有默认参数
        # 选课系统 专门给面向对象编程的时候 的函数准备的
    # 特性      @property
# class Person:
#     @staticmethod
#     def login():
#         pass
# class Teacher(Person):
#     pass

# 调用
    # 对象名.动态属性()/类名.动态属性(对象)
    # 类名.静态属性/对象名.静态属性
    # 类名.类方法()/对象名.类方法()
    # 类名.静态方法/对象名.静态方法()

# 对象的命名空间中能存的:
    # 属性
# 对象能调用的:
    # 对象属性
    # 类中的普通方法

# 私有的
    # __名字
        # 静态属性
        # 动态属性
        # 类方法
        # 静态方法
        # 属性
    # 私有的有什么特点
        # 只能在类的内部调用
        # 不能被继承
    # 什么时候用私有的?
        # 当不想被外部调用也不想被继承,只想在类内部使用的时候
        # 当在外部使用的时候,想给用户的使用前\后直接加上某些功能
            # 私有 + property使用

# 3w1h
# what  这个东西是什么
# where 在哪儿用
# why   为什么这么用
# how   怎么用

# class A:
#     def __init__(self,name):
#         self.__name = name
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,new_name):
#         if type(new_name) is str:
#             self.__name = new_name
# obj = A('alex')
# obj.name = 123
# print(obj.name)

# 看视频
# 博客
# 思维导图

# 反射
# 内置方法
