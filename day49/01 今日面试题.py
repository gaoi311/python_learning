"""
1. 谈谈你对面向对象的理解？
对象 = 数据 + 方法

2. Python面向对象中的继承有什么特点？
3. 面向对象深度优先和广度优先是什么？

必须得了解：
MRO
深度优先 广度优先 C3算法  => http://python.jobbole.com/85685/


4. 面向对象中super的作用？
    在子类中执行父类的方法
5. 列举面向对象中特殊成员(带双下划线的特殊方法，如：__new__、__init__、__call__等)
    __new__(): 开辟空间，创建对象
    __init__(): 初始化对象，对象属性的赋值
    __call__(): 对象()直接执行的代码
    __str__(): print(对象)时执行的
    __repr__(): 解释器环境下直接输入对象展示的内容
    __len__(): len()
    __del__(): 析构
    __hash__():
    __eq__():
    __setitem__():
    __getitem__():
    __delitem__():
6. 静态方法和类方法区别？

"""


class Person(object):
    name = "黄袍哥"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def yongshou():
        print("不可描述...")

    @classmethod
    def haiyongshou(cls):
        """
        修改静态属性
        :return:
        """
        cls.name = "蝇蝇"
        print("再次不可描述...")
        print(cls.name)

    @property
    def age(self):
        return "本是同根生，相煎何太急！"



Person.yongshou()
Person.haiyongshou()
p1 = Person("康抻")
print(p1.age)


