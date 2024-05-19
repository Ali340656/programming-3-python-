from socket import *
from threading import *

def send_message(s1):
    while True:
        msg=input()
        s1.send(bytes(msg,"utf-8"))

def recive_message(s1):
    while True:
        msg=s1.recv(500)
        print(msg.decode("utf-8"))


s1=socket(AF_INET,SOCK_STREAM)
s1.connect(("127.0.0.1",1234))
msg=s1.recv(500)
print(msg.decode("utf-8"))
t1=Thread(target=send_message,args=(s1,))
t2=Thread(target=recive_message,args=(s1,))
t1.start
t2.start