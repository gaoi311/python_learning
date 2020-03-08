'''
3,模拟英雄联盟写一个游戏人物的类（升级题）.
  要求:
  (1)创建一个 Game_role的类.
  (2) 构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
  (3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
      例: 实例化一个对象 盖伦,ad为10, hp为100
      实例化另个一个对象 剑豪 ad为20, hp为80
      盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.
'''


# class GameRole:
#     def __init__(self, name, ad, hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def attack(self,p):
#         p.hp = p.hp - self.ad
#         print('%s 攻击 %s,%s 掉了%s血,还剩%s血' %(self.name,p.name,p.name,self.ad,p.hp))
#
# p1 = GameRole('盖伦',20,500)
# p2 = GameRole('亚索',50,200)
# p1.attack(p2)
# print(p2.hp)

# 组合: 给一个类的对象封装一个属性,这个属性是另一个类的对象.

# 版本一：添加武器：斧子，刀，枪，棍，棒...,
# 代码不合理: 人物利用武器攻击别人,你的动作发起者是人,而不是武器.
# class GameRole:
#     def __init__(self, name, ad, hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def attack(self,p):
#         p.hp = p.hp - self.ad
#         print('%s 攻击 %s,%s 掉了%s血,还剩%s血' %(self.name,p.name,p.name,self.ad,p.hp))
#
# class Weapon:
#     def __init__(self,name,ad):
#         self.name = name
#         self.ad = ad
#     def fight(self,p1,p2):
#         p2.hp = p2.hp - self.ad
#         print('%s 用%s打了%s,%s 掉了%s血,还剩%s血'\
#               % (p1.name,self.name,p2.name,p2.name,self.ad,p2.hp))
#
# p1 = GameRole('大阳哥',20,500)
# p2 = GameRole('印度阿宁',50,200)
# axe = Weapon('三板斧',60)
# broadsword = Weapon('屠龙宝刀',100)
#
# axe.fight(p1,p2)
# broadsword.fight(p2,p1)

# p1.attack(p2)

# 版本二:
class GameRole:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self,p):
        p.hp = p.hp - self.ad
        print('%s 攻击 %s,%s 掉了%s血,还剩%s血' %(self.name,p.name,p.name,self.ad,p.hp))

    def armament_weapon(self,wea):
        self.wea = wea


class Weapon:
    def __init__(self,name,ad):
        self.name = name
        self.ad = ad
    def fight(self,p1,p2):
        p2.hp = p2.hp - self.ad
        print('%s 用%s打了%s,%s 掉了%s血,还剩%s血'\
              % (p1.name,self.name,p2.name,p2.name,self.ad,p2.hp))

p1 = GameRole('大阳哥',20,500)
p2 = GameRole('印度阿宁',50,200)
axe = Weapon('三板斧',60)
broadsword = Weapon('屠龙宝刀',100)
# print(axe)
p1.armament_weapon(axe)  # 给大阳哥 装备了三板斧这个对象.
# print(p1.wea)
# print(p1.wea.name)
# print(p1.wea.ad)
p1.wea.fight(p1,p2)