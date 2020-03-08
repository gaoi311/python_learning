import os
import subprocess


# r = os.popen('ipconfig')

r = subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

# subprocess.Popen(cmd,shell=True,subprocess.stdout,subprocess.stderr)
# cmd : 代表系统命令
# shell = True   代表这条命令是 系统命令,告诉操作系统,将cmd当成系统命令去执行
# stdout   是执行完系统命令之后,用于保存结果的一个管道
# stderr   是执行完系统命令之后,用于保存错误结果的一个管道
stdout = r.stdout.read().decode('gbk')
stderr = r.stderr.read().decode('gbk')
print('正确的返回结果:',stdout)
print('错误的返回结果:',stderr)
print('错误的返回结果:',stderr)

