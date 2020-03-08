import sys
print(sys.path)
sys.path.append('D:\sylar\python_workspace')
import aaa
# 模块没导入之前在哪儿?
# 在硬盘上

# 安装python
# python整个包的结构不变
# 它会记录一个安装目录
# 其他所有目录都是根据安装目录来写死的
# 'D:\\sylar\\python_workspace\\day22',  是你当前运行的脚本所在的目录
# 'D:\\sylar\\python_workspace\\day22'   是pycharm在你打开项目的时候给你添加进来的项目根目录
# 剩余所有都是python内置的目录
    # 内置模块的导入
    # 第三方模块的导入
# 内置模块的导入和第三方模块的导入都不需要你操心了
# 自定义的模块能否被导入
    # 看sys.path当中 是否存在你要导入的文件 所在的目录

# 总结
    # 模块的搜索路径全部存储在sys.path列表中
    # 导入模块的顺序,是从前到后找到一个符合条件的模块就立即停止不再向后寻找
    # 如果要导入的模块和当前执行的文件同级
        # 直接导入即可
    # 如果要导入的模块和当前执行的文件不同级
        # 需要把要导入模块的绝对路径添加到sys.path列表中
