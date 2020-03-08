from threading import Timer# 定时器


def func():
    print('就是这么nb!')

Timer(2.5,func).start()
# Timer(time,func)
# time：睡眠的时间，以秒为单位
# func：睡眠时间之后，需要执行的任务

