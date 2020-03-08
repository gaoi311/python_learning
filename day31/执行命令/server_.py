import socket
import subprocess

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()

conn,addr = sk.accept()
while 1:
    cmd = conn.recv(1024).decode('utf-8')
    r = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout = r.stdout.read()
    stderr = r.stderr.read()
    if stderr:
        conn.send(stderr)
    else:
        conn.send(stdout)

conn.close()
sk.close()

# dir
