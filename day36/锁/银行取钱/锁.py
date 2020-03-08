from multiprocessing import Lock

l = Lock()

l.acquire()# 拿走钥匙，锁门，不让其他人进屋

l.release()# 释放锁。  还钥匙，开门，允许其他人进屋

