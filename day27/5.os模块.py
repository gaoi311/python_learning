import os
# print(os.getcwd())  # 在哪个地方执行这个文件,getcwd的结果就是哪个路径
# print(__file__)
# os.chdir("D:/sylar/python_workspace/day25/")
# print(os.getcwd())

# print(os.curdir)
# print(os.pardir)

# 创建文件夹/删除文件夹
# import os
# os.mkdir('dir')  # ftp 网盘
# os.mkdir('dir/dir5')  # ftp 网盘
# os.makedirs('dir2/dir3/dir4',exist_ok=True)

# os.remove('dir2/dir3/dir4/aaa.py')
# os.rmdir('dir2/dir3/dir4')  # 不能删除一个非空文件夹
# os.removedirs('dir2/dir3/dir4')
# 递归向上删除文件夹,只要删除当前目录之后 发现上一级目录也为空了,就把上一级目录也删掉.
# 如果发现上一级目录有其他文件,就停止

# print(os.listdir('D:\sylar\python_workspace'))

# print(os.stat(r'D:\sylar\python_workspace\aaa.py'))
# print(os.sep)  # 当前你所在的操作系统的目录分割符 \   /a/dir/dir2
# print([os.linesep])  #输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
# print(os.pathsep) #   输出用于分割文件路径的字符串 win下为;,Linux下为:
# print(os.name) # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'


# 学生选课系统
# base_path = 'D:\sylar\python_workspace'
# s = 'day25'
# os.sep.join(base_path,s)
# if os.name == 'nt':
#     '\\'.join(base_path,s)
# else:
#     '/'.join(base_path, s)

# os.system('dir')  # 删除文件 copy文件
# ret = os.popen('dir')  # 查看当前路径 查看某些信息
# print(type(ret.read()))

# print(os.environ)

# print([os.path.abspath('D:/sylar/python_workspace/day25/5.os模块.py')])
# print([os.path.abspath('4.sys模块.py')])
# print(os.path.split('D:/sylar/python_workspace/day25/5.os模块.py'))
# print(os.path.split('D:/sylar/python_workspace/day25'))
# print(os.path.dirname('D:/sylar/python_workspace/day25'))
# print(os.path.dirname('D:/sylar/python_workspace/day25/5.os模块.py'))
# print(os.path.basename('D:/sylar/python_workspace/day25'))
# print(os.path.basename('D:/sylar/python_workspace/day25/5.os模块.py'))
# print(os.path.exists('D:/sylar/python_workspace/day25/6.os模块.py'))
# print(os.path.isfile('D:/sylar/python_workspace/day25/5.os模块.py'))
# print(os.path.isfile('D:/sylar/python_workspace/day25'))
# print(os.path.isdir('D:/sylar/python_workspace/day25/5.os模块.py'))
# print(os.path.isdir('D:/sylar/python_workspace/day25'))

# ret = os.path.join('D:/sylar/python_workspace/day25','aaa','bbb')
# print(os.path.abspath(ret))

# print(os.path.getsize(r'D:\sylar\python_workspace\day25\4.sys模块.py'))
# print(os.path.getsize(r'D:\sylar\python_workspace\day25'))
# print(os.path.getsize(r'D:\sylar\python_workspace\day24'))
# print(os.path.getsize(r'D:\sylar\python_workspace\day23'))

# 统计文件夹中所有的文件的总size


# 计算器
# 发红包
# 计算时间差 : 计算两个时间之间的格式化时间差
# 统计文件夹中所有的文件的总size