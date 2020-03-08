# 运行一个py文件的两种方式
# 1.以模块的形式运行
# import my_module
# if __name__ == '__main__':
#     my_module.login()
# 2.直接pycharm运行 cmd运行
#   ----以脚本的形式运行
#   那么需要在本文件中直接打印的代码上加上
#   if __name__ == '__main__':

# 在编写py文件的时候
    # 所有不在函数和类中封装的内容都应该写在
    # if __name__ == '__main__':下面
# import sys
# import my_module
# sys.modules
# {'sys':文件的内存地址,
# 'my_module': my_module的地址
# '__main__':当前直接执行文件所在的地址}
# 存储了所有导入的文件的名字和这个文件的内存地址

# 再使用反射自己模块中的内容的时候
# import sys
# getattr(sys.modules[__name__],变量名)
