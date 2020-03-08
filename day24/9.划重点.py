# import 模块
# 导入这个模块之后 模块内的所有名字 就都可以通过模块来引用了
# 模块名.名字

# from 模块 import 名字
# 导入这个模块中的某个名字之后,这个名字就可以直接使用了
# 名字是变量 直接用
# 名字是函数 函数名()就是调用
# 名字是类名 类名()就是实例化

# 模块的循环引用 - 不能

# 把模块当成脚本运行 :
    # 你希望 某一段代码 在被当做模块导入的时候 不要执行
    # 就把它卸载 if __name__ == '__main__':下面

# sys.path 一个自定义模块能否被导入,就看sys.path列表中有没有这个模块所在的绝对路径
# import 模块名  # ModuleNotFoundError : No module named '模块名'

# 包
# 从包中导入模块,要注意这个包所在的目录是否在sys.path
# from aaa.bbb.ccc import get  # 正确的
# from bbb.ccc import get  # ModuleNotFoundError: No module named 'bbb'
# get.func()

# 如果是直接导入一个包,那么相当于执行了这个包中的__init__文件
# 并不会帮你把这个包下面的其他包以及py文件自动的导入到内存
# 如果你希望直接导入包之后,所有的这个包下面的其他包以及py文件都能直接通过包来引用
# 那么你要自己处理__init__文件

