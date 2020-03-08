'''
day18天作业及默写
1,完成下列功能:
  1.1创建一个人类Person,再类中创建3个静态变量(静态字段)
    animal = '高级动物'
    soup = '有灵魂'
    language = '语言'
  1.2在类中定义三个方法,吃饭,睡觉,工作.
  1.3在此类中的__init__方法中,给对象封装5个属性:国家,姓名,性别,年龄,  身高.
  1.4实例化四个人类对象:
    第一个人类对象p1属性为:中国,alex,未知,42,175.
    第二个人类对象p2属性为:美国,武大,男,35,160.
    第三个人类对象p3属性为:你自己定义.
    第四个人类对象p4属性为:p1的国籍,p2的名字,p3的性别,p2的年龄,p3  的身高.
  1.5 通过p1对象执行吃饭方法,方法里面打印:alex在吃饭.
  1.6 通过p2对象执行吃饭方法,方法里面打印:武大在吃饭.
  1.7 通过p3对象执行吃饭方法,方法里面打印:(p3对象自己的名字)在吃饭.
  1.8 通过p1对象找到Person的静态变量 animal
  1.9 通过p2对象找到Person的静态变量 soul
  2.0 通过p3对象找到Person的静态变量 language

2,通过自己创建类,实例化对象
  在终端输出如下信息
  小明，10岁，男，上山去砍柴
  小明，10岁，男，开车去东北
  小明，10岁，男，最爱大保健
  老李，90岁，男，上山去砍柴
  老李，90岁，男，开车去东北
  老李，90岁，男，最爱大保健
  老张…

3,模拟英雄联盟写一个游戏人物的类（升级题）.
  要求:
  (1)创建一个 Game_role的类.
  (2) 构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
  (3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
      例: 实例化一个对象 盖伦,ad为10, hp为100
      实例化另个一个对象 剑豪 ad为20, hp为80
      盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.

'''


# class Person:
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#
#     def __init__(self, country, name, sex, age, hight):
#         self.country = country
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.hight = hight
#
#     def eat(self):
#         print('%s吃饭' % self.name)
#
#     def sleep(self):
#         print('睡觉')
#
#     def work(self):
#         print('工作')
#
# p1 = Person('菲律宾','alex','未知',42,175)
# p2 = Person('美国','武大','男',35,160)
# p3 = Person('中国','小西','男',18,185)
# #  第四个人类对象p4属性为:p1的国籍,p2的名字,p3的性别,p2的年龄,p3  的身高.
# p4 = Person(p1.country,p2.name,p3.sex,p2.age,p3.hight)
# p1.eat()
# p2.eat()
# p3.eat()
# print(p4.__dict__)

'''
  小明，10岁，男，上山去砍柴
  小明，10岁，男，开车去东北
  小明，10岁，男，最爱大保健
  老李，90岁，男，上山去砍柴
  老李，90岁，男，开车去东北
  老李，90岁，男，最爱大保健
  老张…
'''


# class HappyDay:
#
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def Chop_wood(self):
#         print('%s %s %s 上山去砍柴' % (self.name,self.age,self.sex))
#
#     def Drive(self):
#         print('%s 开车去东北' % self.name)
#
#     def Great_health_care(self):
#         print('%s 最爱大宝剑' % self.name)
#
# p1 = HappyDay('小名',10, '男')
# p1.Drive()

