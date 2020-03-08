from multiprocessing import Process
import time

def func1():
    for i in range(65,90):
        print(chr(i))
        time.sleep(0.5)

def func():
    for i in range(10):
        print(i)
        time.sleep(0.5)

if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    p1 = Process(target=func1)
    p1.daemon = True
    p1.start()
    # time.sleep(2)

    # print(p.is_alive())
    # p.terminate()
    # p.join()
    # print(p.is_alive())
    # print(p.pid,p.name)
    # for i in range(10,21):
    #     print(i)
    #     time.sleep(1)

