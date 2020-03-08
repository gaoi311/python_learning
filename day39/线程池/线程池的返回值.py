from concurrent.futures import ThreadPoolExecutor
import time


def func(num):
    sum = 0
    # time.sleep(5)
    # print(num) # 异步的效果
    for i in range(num):
        sum += i ** 2
    return sum

t = ThreadPoolExecutor(20)

# 下列代码是用map的方式提交多个任务，对应 拿结果的方法是__next__()  返回的是一个生成器对象
res = t.map(func,range(1000))
t.shutdown()
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())






# 下列代码是用for + submit提交多个任务的方式，对应拿结果的方法是result
# res_l = []
# for i in range(1000):
#     re = t.submit(func,i)
#     res_l.append(re)
# # t.shutdown()
# [print(i.result()) for i in res_l]
# 在Pool进程池中拿结果，是用get方法。   在ThreadPoolExecutor里边拿结果是用result方法