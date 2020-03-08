# 什么是异常?异常和错误的区别
    # Error  语法错误   比较明显的错误 在编译代码阶段就能检测出来
    # Iteration 异常  在执行代码的过程中引发的异常
# 异常发生之后的效果
    # 一旦在程序中发生异常,程序就不再继续执行了
# 如何看报错信息
    # l = []
    # l[3]
    # def func():
    #     import time
    #     time.ti()
    # def main():
    #     func()
    # main()
# 最简单的异常处理
# l = ['登录','注册','退出']
# for i in enumerate(l,1):
#     print(i[0],i[1])
# try:
#     num = int(input('num :'))
#     print(l[num-1])
# except IndexError:
#     print('请输入一个数字')
# 多分支异常处理
# l = ['登录','注册','退出']
# for i in enumerate(l,1):
#     print(i[0],i[1])
# try:
#     num = int(input('num :'))
#     print(l[num-1])
# except ValueError:
#     print('请输入一个数字')
# except IndexError:
#     print('您输入的数字无效')

# 万能异常
# try:
#     name  # NameError
#     dic = {}
#     dic['key']
# except Exception as 变量名:
#     print(type(变量名),变量名,变量名.__traceback__.tb_lineno)

# 万能异常和其他分支合作 : 万能异常永远要放在所有except的最后
# try:
#     name
#     [][3]
#     import a
# except NameError:pass
# except IndexError:pass
# except Exception:pass

# 异常处理的其他机制
# try:
#     name
#     [][3]
# except IndexError:print('index error')
# except NameError:print('name error')

# try:
#     name
#     [][3]
# except (IndexError,NameError) as e:
#     print(e)

# try:
#     a = 1
#     # name
#     # [][3]
# except NameError:
#     print('name error')
# except Exception:
#     print('万能异常')
# else: # try中的代码正常执行 没有异常的时候会执行else中的代码
#     print('执行else了')
# finally: # 无论如何都会执行 操作系统资源归还的工作
#     print('执行finally了')
# try:
#     f = open('file','w')
#     # f.read()
#     exit()
# except:pass
#     # 复杂的逻辑
# finally:
#     f.close()
#     print('执行我啦')
#
# def func():
#     try:
#         f = open('file', 'w')
#         return f.read()
#     finally:
#         f.close()
#         print('执行我了')
#
# func()

# try/except
# try/except/else
# try/except/else/finally
# try/except/finally
# try/finally

# 主动抛异常
# try:
#     num = int(input('>>>'))
# except Exception:
#     print('在出现了异常之后做点儿什么,再让它抛异常')
#     raise  # 原封不动的抛出try语句中出现的异常

# 自定义异常
# raise NameError('这是一个name error的异常')
# class EvaException(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#
# raise EvaException('这是一个什么什么错误,有什么问题')

# 断言
# assert 布尔值
# assert True
# if False:
#     print(1234234)
# else:
#     raise AssertionError

# 使用异常处理的注意事项
# 断言 assert raise 主动抛异常
# 异常处理
    # try/except
    # try/except/else
    # try/except/else/finally
    # try/except/finally
    # try/finally


# strat.py
# if __name__ == '__main__':
#     try:
#         core.main()
#     except Exception:
#         pass

# 尽量少用异常处理
# 能通过逻辑规避的应该代码逻辑规避掉
# 应该对某一句/几句话来进行处理

# 最后 在外层添加一个大的异常处理