from socket import *
from threading import *

def send(s1):
    while True:
        msg=input()
        s1.send(bytes(msg,"utf-8"))

def recive(s1):
    while True:
        msg=s1.recv(500)
        print(msg.decode("utf-8"))

s1=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=1234
s1.bind((host,port))
print("socket is listening")
print ("socket binded to ",port) 
s1.listen(5)
while True:
    clientSocket,clientAdress=s1.accept()
    print("",clientAdress)
    clientSocket.send(bytes("welcome","utf-8"))
    t1=Thread(target=send,args=(clientSocket,))
    t2=Thread(target=recive,args=(clientSocket,))
    t1.start
    t2.start