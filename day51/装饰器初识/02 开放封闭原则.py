"""
不改变函数原来的调用方式 动态地 给函数 添加功能
开放 封闭原则
1. 对添加新功能是开放的
2. 硬改已经存在的代码
"""


def create_people():
    # print("加口唾沫~")  # 违背了封闭原则
    print("抓把泥，捏个人，吹口气， 活了！")


def koushui_create_people(arg):
    def inner():
        print("加口唾沫")
        arg()
        print("上个色儿~")
    return inner

# create_people()
# create_people()
# create_people()

# koushui_create_people()
# koushui_create_people()
# koushui_create_people()

# ret = koushui_create_people(create_people)
# print(ret)
# ret()


create_people = koushui_create_people(create_people)


create_people()
# 加口唾沫~
# 抓把泥，捏个人，吹口气， 活了！


