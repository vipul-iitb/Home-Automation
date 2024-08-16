import socket
import os

TCP_IP = '192.168.43.126'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
        MESSAGE = "."
        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        print (data)

        if data == "hello":
                os.system("espeak 'hello sir phoenix at your service'")
        if data == "what is your name":
                os.system("espeak 'my name is phoenix and i am your personal assisstant'")
        else:
                os.system("espeak 'unkown commnad'")


s.close()


