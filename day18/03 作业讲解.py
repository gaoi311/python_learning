# day15天作业及默写
# 1，暴力摩托程序（完成下列需求）：
# 1.1
# 创建三个游戏人物，分别是：
# •    苍井井，女，18，攻击力ad为20，血量200
# •    东尼木木，男，20，攻击力ad为30，血量150
# •    波多多，女，19，攻击力ad为50，血量80
# 1.2
# 创建三个游戏武器，分别是：
# •    平底锅，ad为20
# •    斧子，ad为50
# •    双节棍，ad为65
#
# 1.3
# 创建三个游戏摩托车，分别是：
#
# •    小踏板，速度60迈
# •    雅马哈，速度80迈
# •    宝马，速度120迈。
#
# 完成下列需求（利用武器打人掉的血量为武器的ad + 人的ad）：

# （1）苍井井骑着小踏板开着60迈的车行驶在赛道上。
# （2）东尼木木骑着宝马开着120迈的车行驶在赛道上。
# （3）波多多骑着雅马哈开着80迈的车行驶在赛道上。


# （4）苍井井赤手空拳打了波多多20滴血，波多多还剩xx血。
# （5）东尼木木赤手空拳打了波多多30滴血，波多多还剩xx血。

# （6）波多多利用平底锅打了苍井井一平底锅，苍井井还剩xx血。
# （7）波多多利用斧子打了东尼木木一斧子，东尼木木还剩xx血。


# （8）苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血。
# （9）波多多骑着小踏板打了骑着雅马哈的东尼木木一斧子，东尼木木哭了，还剩xx血。

class GameRole:
    def __init__(self,name,sex,age,ad,hp):
        self.name = name
        self.sex = sex
        self.age = age
        self.ad = ad
        self.hp = hp

    def attack(self,p):
        p.hp = p.hp - self.ad
        print('%s赤手空拳打了%s%s滴血，%s还剩%s血' %(self.name,p.name,self.ad,p.name,p.hp))


    def add_moto(self,mo):
        self.mo = mo

    def add_weapon(self,wea):
        self.wea = wea

    def road_rush(self,p1):
        p1.hp = p1.hp - self.ad - self.wea.ad
        print('%s骑着%s打了骑着%s的%s一%s，%s哭了，还剩%s血' \
              %(self.name,self.mo.name,p1.mo.name,p1.name,self.wea.name,p1.name,p1.hp))




class Weapon:
    def __init__(self,name,ad):
        self.name = name
        self.ad = ad

    def fight(self,p1,p2):
        p2.hp = p2.hp - p1.ad - self.ad
        # print(' %s利用%s打了%s一%s，%s还剩%s血' %(p1.name,self.name,p2.name,self.name,p2.name,p2.hp))
        print('{0}利用{1}打了{2}一{1},{2}还剩{3}血'.format(p1.name,self.name,p2.name,p2.hp))


class Moto:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def drive(self,p1):
        print('%s骑着%s开着%d迈的车行驶在赛道上' % (p1.name,self.name,self.speed))

p1 = GameRole('苍井井','女',18,20,200)
p2 = GameRole('东尼木木','男',20,30,150)
p3 = GameRole('波多多','女',19,50,80)

w1 = Weapon('平底锅',20)
w2 = Weapon('斧子',50)
w3 = Weapon('双节棍',65)


m1 = Moto('小踏板',60)
m2 = Moto('雅马哈',80)
m3 = Moto('宝马',120)

# p1.add_moto(m1)  # 组合: 给p1 对象封装了一个属性,属性值 m1这个对象
# p1.mo.drive(p1)

# p1.attack(p3)

# 波多多利用平底锅打了苍井井一平底锅，苍井井还剩xx血。
# p3.add_weapon(w1)  # 组合: 给p1 对象封装了一个属性,属性值 w1这个对象
# p3.wea.fight(p3,p1)


# 苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血。
# p1.add_moto(m3)
# p1.add_weapon(w3)
# p2.add_moto(m1)
p1.road_rush(p2)



# 2，定义一个类，计算圆的周长和面积。
from math import pi

class Circle:

    def __init__(self,r):
        self.r = r

    def area(self):
        return round(self.r ** 2 * pi,2)

    def perimeter(self):
        return round(self.r * 2 * pi,2)
# c1 = Circle(5)
# print(c1.area())
# print(c1.perimeter())




# 3，定义一个圆环类，计算圆环的周长和面积（升级题）。

# class Ring:
#
#     def __init__(self,r1,r2):
#         self.r1 = r1
#         self.r2 = r2
#
#     def area(self):
#         return round(self.r1 ** 2 * pi - self.r2 ** 2 * pi, 2)
#
#     def perimeter(self):
#         return round(self.r1 * 2 * pi + self.r2 * 2 * pi, 2)
#
# r1 = Ring(6,3)
# print(r1.area())
# print(r1.perimeter())

# 组合的思想
# class Ring:
#
#     def __init__(self,r1,r2):
#         self.r1 = Circle(r1)
#         self.r2 = Circle(r2)
#
#     def area(self):
#         return self.r1.area() - self.r2.area()
#
#     def perimeter(self):
#         return self.r1.perimeter() + self.r2.perimeter()
#
# r = Ring(6,3)
# print(r1.area())
# print(r1.perimeter())