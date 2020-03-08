# 属性的初识
# class Person:
#
#     def __init__(self,name,hight,weight):
#         self.name = name
#         self.__hight = hight
#         self.__weight = weight
#
#     @property
#     def bmi(self):
#         return '%s 的bmi 值%s' %(self.name,self.__weight / self.__hight ** 2)
#
# p1 = Person('大阳哥',1.68,70)
# # print(p1.bmi())
# print(p1.bmi)
# # 属性  : 将一个方法  伪装成一个 属性,在代码的级别上没有本质的提升,但是让其看起来跟合理.
# print(p1.name)
# p1.name = 'alex'
# print(p1.name)

# 属性的改
class Person:
    def __init__(self,name,age):
        self.name = name
        if type(age) is int:
            self.__age = age
        else:
            print( '你输入的年龄的类型有误,请输入数字')
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,a1):
        '''判断,你修改的年龄必须是数字'''
        if type(a1) is int:
            self.__age = a1
        else:
            print('你输入的年龄的类型有误,请输入数字')

    @age.deleter
    def age(self):
        del self.__age


p1 = Person('帅哥',20)
print(p1.age)
# print(p1.__dict__)
# p1.age = 23
# print(p1.age)
del p1.age

# property : 类似于bmi这种,area,周长....  ***
# @age.setter  **
# @age.deleter *
