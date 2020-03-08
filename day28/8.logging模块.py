# 功能
    # 1. 日志格式的规范
    # 2. 操作的简化
    # 3. 日志的分级管理

# logging不能帮你做的事情
    # 自动生成你要打印的内容
# 需要程序员自己在开发的时候定义好 :
    # 在哪些地方需要打印,要打印的内容是什么,内容的级别

# logging模块的使用 :
    # 普通配置型 简单的 可定制化差
    # 对象配置型 复杂的 可定制化强

# 认识日志分级

# import logging
# logging.debug('debug message')      # 调试模式
# logging.info('info message')        # 基础信息
# logging.warning('warning message')  # 警告
# logging.error('error message')      # 错误
# logging.critical('critical message')# 严重错误


# import logging
#
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('debug message')      # 调试模式
# logging.info('info message')        # 基础信息
# logging.warning('warning message')  # 警告
# logging.error('error message')      # 错误
# logging.critical('critical message')# 严重错误

# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log')
# logging.debug('debug message')      # 调试模式
# logging.info('info message')        # 基础信息
# logging.warning('warning message')  # 警告
# logging.error('error message')      # 错误
# logging.critical('critical message')# 严重错误

# basicConfig
# 不能将一个log信息既输出到屏幕 又输出到文件

# logger对象的形式来操作日志文件

# 创建一个logger对象
# 创建一个文件管理操作符
# 创建一个屏幕管理操作符
# 创建一个日志输出的格式

# 文件管理操作符 绑定一个 格式
# 屏幕管理操作符 绑定一个 格式

# logger对象 绑定 文件管理操作符
# logger对象 绑定 屏幕管理操作符

import logging
# 创建一个logger对象
logger = logging.getLogger()
# 创建一个文件管理操作符
fh = logging.FileHandler('logger.log',encoding='utf-8')
# 创建一个屏幕管理操作符
sh = logging.StreamHandler()
# 创建一个日志输出的格式
format1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 文件管理操作符 绑定一个 格式
fh.setFormatter(format1)
# 屏幕管理操作符 绑定一个 格式
sh.setFormatter(format1)
logger.setLevel(logging.DEBUG)
# logger对象 绑定 文件管理操作符
# logger.addHandler(fh)
# logger对象 绑定 屏幕管理操作符
logger.addHandler(sh)

logger.debug('debug message')      # 调试模式
logger.info('我的信息')        # 基础信息
logger.warning('warning message')  # 警告
logger.error('error message')      # 错误
logger.critical('critical message')# 严重错误




