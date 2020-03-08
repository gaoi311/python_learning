# s1 = 'fdsajkf'
# count = 0
# for i in s1:
#     count += 1
# print(count)
#
# l1 = [1,2,3]
# count = 0
# for i in l1:
#     count += 1
# print(count)
#
# def my_len(argv):
#     count = 0
#     for i in argv:
#         count += 1
#     return count



# 文件:
# 1,'alex','未知',1356666666,IT

# def add(name,sex,phone,job):
#     '''100行代码,'''
#     pass
#
# def remove(name,sex,phone,job):
#     '''100行代码,'''
#     pass
#
# def update(name,sex,phone,job):
#     '''100行代码,'''
#     pass
#
# def find(name,sex,phone,job):
#     '''100行代码,'''
#     pass
# add('alex','未知',1356666666,'IT')
# remove('alex','未知',1356666666,'IT')
#
# class file:
#     def __init__(self,name,sex,phone,job):
#         self.name = name
#         self.sex = sex
#         self.phone = phone
#         self.job = job
#
#     def add(self):
#         '''100行代码,'''
#         pass
#
#     def remove(self):
#         '''100行代码,'''
#         pass
#
#     def update(self):
#         '''100行代码,'''
#         pass
#
#     def find(self):
#         '''100行代码,'''
#         pass
# f1 = file('alex','未知',1356666666,'IT')
# f1.add()
# f1.remove()

# 类:具有相同属性和技能的一类事物.
# 人类:
# 对象: 具体的类的表现,具体的实实在在的一个实例
# 人是一类,大阳哥是一个对象.
# 狗是一类,我家养的旺财是一个对象.

# class Person:
#     '''类体:两部分:变量部分,方法(函数)部分'''
#     mind = '有思想'  # 变量,静态变量,静态字段
#     animal = '高级动物'
#     faith = '有信仰'
#     def __init__(self):
#         print(self)
#         print(666)
#     # def __init__(self, name, age, sex, hobby):
#     #     print(666)
#     def work(self):  # 方法,函数,动态变量
#         print(self)
#         print('人类都会工作...')
#     def shop(self):
#         print('人类可以消费....')
#
# # 类名的角度
#     # 操作类中的静态变量
#         # 1, Person.__dict__ 查询类中的所有的内容 (不能进行增删改操作)
# # print(Person.__dict__)
# # print(Person.__dict__['faith'])
# # Person.__dict__['mind'] = '无脑'
# # print(Person.__dict__['mind'])
#         # 2, 万能的  .  对类中的单个的变量进行增删改查,用 万能的 点
# # print(Person.mind)
# # print(Person.animal)  # 查
# # Person.money = '运用货币'  # 增
# # Person.mind = '无脑的' # 改
# # del Person.mind
# # print(Person.__dict__)
#
#     #操作类中的方法  (工作中基本不用类名去操作)
# # Person.work(111)
#
# # 对象的角度
# ret = Person()  # 类名+()的这个过程:实例化的过程(创建一个对象的过程),
#           # Person() 实例化对象,实例,对象.
# print(ret)
# #1,只要类名+() 产生一个对象,自动执行类中的__init__方法.



class Person:
    '''类体:两部分:变量部分,方法(函数)部分'''
    mind = '有思想'  # 变量,静态变量,静态字段
    animal = '高级动物'
    faith = '有信仰'

    def __init__(self,name,age,hobby):
        self.name = name  #  Person.money = '运用货币'
        self.age = age
        self.hobby = hobby

    def work(self):  # 方法,函数,动态变量

        print('%s都会工作...' %self.name)
    def shop(self):

        print('人类可以消费....')

# 类名的角度
    # 操作类中的静态变量
        # 1, Person.__dict__ 查询类中的所有的内容 (不能进行增删改操作)
# print(Person.__dict__)
# print(Person.__dict__['faith'])
# Person.__dict__['mind'] = '无脑'
# print(Person.__dict__['mind'])
        # 2, 万能的  .  对类中的单个的变量进行增删改查,用 万能的 点
# print(Person.mind)
# print(Person.animal)  # 查
# Person.money = '运用货币'  # 增
# Person.mind = '无脑的' # 改
# del Person.mind
# print(Person.__dict__)

    #操作类中的方法  (工作中基本不用类名去操作)
# Person.work(111)

# 对象的角度
# ret = Person('alex',1000, 'oldwomen')  # 类名+()的这个过程:实例化的过程(创建一个对象的过程),
          # Person() 实例化对象,实例,对象.
# print(ret)


#1, 类名+()产生一个实例(对象,对象空间.)
#2, 自动执行类中的__init__方法,将对象空间传给__init__的self参数,
#3, 给对象封装相应的属性.
# print(ret.__dict__)

# 对象的角度
    # 操作对象中的静态变量
        #1, __dict__ 查询对象中的所有的内容
        #2, 万能的.  万能的 点.
# print(ret.name)  # 查
# ret.high = 175  # 增
# del ret.name  # 删
# ret.age = 73 # 改
# print(ret.__dict__)
    # 对象操作类中的静态变量 : 只能查询.
# print(ret.mind)

    # 对象调用类中的方法  (工作中 通过对象执行类中的方法,而不是通过类名)
# ret.shop()
# print(ret)

bigsum = Person('大阳哥',39, '非男')
india_ning = Person('印度阿宁',19, '女')
bigsum.work()
india_ning.work()

