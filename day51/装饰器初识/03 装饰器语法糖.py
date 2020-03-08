# 语法糖
def koushui_create_people(arg):
    def inner():
        print("加口唾沫")
        arg()
        print("上个色儿")
    return inner


@koushui_create_people
def create_people():
    # print("加口唾沫~")  # 违背了封闭原则
    print("抓把泥，捏个人，吹口气， 活了！")


create_people()

