
import time
# 1024*15 / 1500000
for i in range(51):
    time.sleep(0.12)
    print('\r'+ i*'=' + '>' + str(i*2) + '%',end='')