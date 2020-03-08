from multiprocessing import Process,Manager


def func(num):
    num[0] -= 1
    print('子进程中的num的值是',num)

if __name__ == '__main__':
    m = Manager()
    num = m.list([1,2,3])
    p = Process(target=func,args=(num,))
    p.start()
    p.join()
    print('父进程中的num的值是',num)