# 模块
# time
    # 时间的格式 : 时间戳 结构化 格式化时间
    # 时间戳time.time <-mktime-结构化time.localtime <-strptime-格式化时间time.strftime
# sys
    # path
    # argv 在执行python文件的时候,在python指令之后的所有内容,以空格隔开都会成为argv的项
    # modules  sys.modules[__name__]
# os
    # mkdir/rmdir/makedirs/removedirs/listdir
    # remove/rename
    # system popen
    # path : join  split basename dirname abspath isdir isfile getsize
# 序列化
    # 把其他格式的数据 转换成 字符串
    # 网络传输 写文件
    # json
        # 能处理的数据类型 : 有限,限制比较多
        # 能使用的语言 : 所有语言
        # 方法 : dump/load  dumps/loads