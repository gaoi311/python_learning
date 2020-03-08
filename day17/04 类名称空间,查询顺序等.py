class Person:
    animal = '高级动物'
    soul = '有灵魂'
    language = '语言'

    def __init__(self, country, name, sex, age, hight):
        self.country = country
        self.name = name
        self.sex = sex
        self.age = age
        self.hight = hight

    def eat(self):
        print('%s吃饭' % self.name)

    def sleep(self):
        print('睡觉')

    def work(self):
        print('工作')


Person.__dict__['sleep'](111)

p1 = Person('菲律宾','alex','未知',42,175)
p2 = Person('菲律宾','alex','未知',42,175)
p3 = Person('菲律宾','alex','未知',42,175)
p1.animal = '禽兽'
print(p1.animal)
#
# print(Person.name)
# p2 = Person('美国','武大','男',35,160)
#
# 查询顺序:
#   对象.属性 : 先从对象空间找,如果找不到,再从类空间找,再找不到,再从父类找....
#   类名.属性 : 先从本类空间找,如果找不到,再从父类找....
#
# 对象与对象之间是互相独立的.
#
# 计算一个类 实例化多少对象.
#
# class Count:
#     count = 0
#     def __init__(self):
#         Count.count = self.count + 1
#
# obj1 = Count()
# obj2 = Count()
#
# print(Count.count)
# count = 0
#
# def func():
#     print(count)
# func()
#
# class Count:
#     count = 0
#     def __init__(self):
#         pass
#
# 通过类名可以更改我的类中的静态变量值
# Count.count = 6
# print(Count.__dict__)
#
# 但是通过对象 不能改变只能引用类中的静态变量
#
# obj1 = Count()
# print(obj1.count)
# obj1.count = 6
#
#
