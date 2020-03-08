from multiprocessing import Process
def func(i):
    print('我是%s'%i)
    # global n
    # print(n)


if __name__ == '__main__':
    n = 100
    addr = ['河南的','山东的','辽宁的','湖南的']
    for i in addr:
        p = Process(target=func,args=(i,))
        p.start()