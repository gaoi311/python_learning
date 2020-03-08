# 什么是反射?
# 用字符串数据类型的变量名来访问这个变量的值
# 反射的方法: getattr hasattr setattr delattr

# class Student:
#     def __init__(self,name):
#         self.name = name
#     def check_course(self):
#         print('check_course')
#     def choose_course(self):
#         print('choose_course')
#     def choosed_course(self):
#         print('查看已选择的课程')
# stu = Student()
# num = input('>>>')
# if num == 'check_course':
#     stu.check_course()
# elif num == 'choose_course':
#     stu.choose_course()
# elif num == 'choosed_course':
#     stu.choosed_course()

# eval 这个东西 明确的写在你的代码里

# 类  静态属性 类方法 静态方法
# 命名空间.XXX == getattr(命名空间,'XXX')
# class Student:
#     ROLE = 'STUDENT'
#     @classmethod
#     def check_course(cls):
#         print('查看课程了')
#
#     @staticmethod
#     def login():
#         print('登录')
# # 反射查看属性
# # print(Student.ROLE)
# # print(getattr(Student,'ROLE'))
#
# # 反射调用方法
# # getattr(Student,'check_course')()  # 类方法
# # getattr(Student,'login')()         # 静态方法
#
# num = input('>>>')
# if hasattr(Student,num):
#     getattr(Student,num)()

# 对象
# 方法 对象属性
# class A():
#     def __init__(self,name):
#         self.name = name
#
#     def func(self):
#         print('in func')
#
# a = A('alex')
# print(a.name)
# print(getattr(a,'name'))
# getattr(a,'func')()

# 模块
# import os   # 别人写好的python代码的结合
# # os.rename('__init__.py','init')
# # getattr(os,'rename')('init','__init__.py') # == os.rename
# rename = os.rename
# rename2 = getattr(os,'rename')
# rename2('__init__.py','init')  # os.rename('__init__.py','init')
# rename('init','init2')          # os.rename('init','init2')

# def wahaha():
#     print('wahaha')
#
# def qqxing():
#     print('qqxing')

# 反射自己模块中的内容  找到自己当前文件所在的命名空间
# wahaha()
# qqxing()

# import sys
# print(sys.modules)
# import 都相当于导入了一个模块
# 模块哪个导入了 哪个没导入 在我的python解释器里应该记录下来
# import sys 是一个模块,这个模块里的所有的方法都是和python解释器相关的
# sys.modules 这个方法 表示所有在当前这个python程序中导入的模块
# '__main__': <module '__main__' from 'D:/sylar/python_workspace/day20/4.反射.py'>
# print(sys.modules['__main__'])
# my_file = sys.modules['__main__']
# my_file.wahaha()
# my_file.qqxing()
# # 'qqxing'
# # 'wahaha'
# getattr(my_file,'wahaha')()
# getattr(my_file,'qqxing')()


# 反射
# hasattr,getattr
# 类名.名字
    # getattr(类名,'名字')
# 对象名.名字
    # getattr(对象,'名字')
# 模块名.名字
    # import 模块
    # getattr(模块,'名字')
# 自己文件.名字
    # import sys
    # getattr(sys.modules['__main__'],'名字')

# 选课系统的代码
# login
# 判断身份 并且根据身份实例化
# 根据每个身份对应的类 让用户选择能够做的事情
class Manager:
    OPERATE_DIC = [
        ('创造学生账号', 'create_student'),
        ('创建课程','create_course'),
        ('查看学生信息','check_student_info'),
    ]
    def __init__(self,name):
        self.name = name
    def create_student(self):
        print('创建学生账号')
    def create_course(self):
        print('创建课程')
    def check_student_info(self):
        print('查看学生信息')

class Student:
    OPERATE_DIC = [
        ('查看所有课程', 'check_course'),
        ('选择课程', 'choose_course'),
        ('查看已选择的课程', 'choosed_course')
    ]
    def __init__(self,name):
        self.name = name
    def check_course(self):
        print('check_course')
    def choose_course(self):
        print('choose_course')
    def choosed_course(self):
        print('查看已选择的课程')

def login():
    username = input('user : ')
    password = input('pwd : ')
    with open('userinfo') as f:
        for line in f:
            user,pwd,ident = line.strip().split('|')   # ident = 'Manager'
            if user == username and pwd == password:
                print('登录成功')
                return username,ident

import sys
def main():
    usr,id = login()
    print('user,id :',usr,id)
    file = sys.modules['__main__']
    cls = getattr(file,id)     #Manager = getattr(当前文件,'Manager')
    obj = cls(usr)
    operate_dic = cls.OPERATE_DIC
    while True:
        for num,i in enumerate(operate_dic,1):
            print(num,i[0])
        choice = int(input('num >>>'))
        choice_item = operate_dic[choice-1]
        getattr(obj,choice_item[1])()
main()
# l = ['a','b','c']
# for num,i in enumerate(l,1):
#     print(num,i)

# class A:
#     def __init__(self,name):
#         self.name = name
#
# a = A('alex')


# # a.name = 'alex_SB'
# # getattr(a,'name')
# setattr(a,'name','alex_SB')
# print(a.name)
# print(a.__dict__)
# del a.name
# print(a.__dict__)
# delattr(a,'name')
# print(a.__dict__)









