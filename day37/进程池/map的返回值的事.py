from multiprocessing import Pool


def func(num):
    num += 1
    print(num)
    return num

if __name__ == '__main__':
    p = Pool(5)
    res = p.map(func,[i for i in range(100)])
    p.close()
    p.join()
    print('主进程中map的返回值',res)
