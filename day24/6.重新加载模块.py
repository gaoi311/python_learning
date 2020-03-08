import aaa
import time
import importlib
aaa.login()
time.sleep(20)
importlib.reload(aaa)  # 表示重新加载
aaa.login()

# 在import之后 再修改这个被导入的模块
# 程序感知不到

# reload这种方式可以强制程序再重新导入这个模块一次
# 非常不推荐你使用