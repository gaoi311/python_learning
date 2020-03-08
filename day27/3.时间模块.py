import time

# 时间戳时间,格林威治时间,float数据类型  给机器用的
    # 英国伦敦的时间  1970.1.1 0:0:0
    # 北京时间 1970.1.1 8:0:0
    # 1533693120.3467407
# 结构化时间,时间对象                   上下两种格式的中间状态
    # 时间对象 能够通过.属性名来获取对象中的值
# 格式化时间,字符串时间,str数据类型      给人看的
    # 可以根据你需要的格式 来显示时间

# print(time.time())   # 时间戳时间
# print(time.strftime('%Y-%m-%d'))  # 格式化时间 str format time
# time_obj = time.localtime()       # 对象数据结构的
# print(time_obj)
# print(time_obj.tm_year)
# print(time_obj.tm_mday)

# print(time.strftime('%Y-%m-%d %A %H:%M:%S'))
# print(time.strftime('%y-%m-%d %A %H:%M:%S'))
# print(time.strftime('%y/%m/%d %H:%M:%S'))
# print(time.strftime('%c'))

# print(time.time())
# print(time.localtime(1500000000))
# print(time.localtime(2000000000))
# time_obj = time.localtime(3000000000)
# format_time = time.strftime('%y-%m-%d %H:%M:%S',time_obj)
# print(format_time)

# 2008-8-8
# struct_time = time.strptime('2008-8-8','%Y-%m-%d')
# print(struct_time)
# print(time.mktime(struct_time))

# 计算本月一号的时间戳时间
# 结构化时间
# struct_time = time.localtime()
# struct_time = time.strptime('%s-%s-1'%(struct_time.tm_year,struct_time.tm_mon),'%Y-%m-%d')
# print(time.mktime(struct_time))
# 格式化时间
# ret = time.strftime('%Y-%m-1')
# struct_time = time.strptime(ret,'%Y-%m-%d')
# print(time.mktime(struct_time))

# 计算器
# 发红包
# 计算时间差 : 计算两个时间之间的格式化时间差
# 统计文件夹中所有的文件的总size