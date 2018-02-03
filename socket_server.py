from socket import *
import subprocess
import threading
import sys
ip_port=('127.0.0.1',8080)
BUFSIZE=1024

socket_server=socket(AF_INET,SOCK_STREAM)
socket_server.bind(ip_port)
socket_server.listen(5)
class server_sw() :
    def main(self) :
        while True :
            try :
                context = self.s.recv(1000)
                for item in session_array :
                    try :
                        item.send(context)#懒得写了甭管它死的活的统统循环一遍
                    except Exception :
                        pass
                #print(context.decode('utf-8'))
            except Exception :
                print('有人离开的聊天室')
                sys.exit()
    def __init__(self,s) :
        self.s = s
        self.main()
session_array = []
while True:
    s,a = socket_server.accept()
    session_array.append(s)
    t = threading.Thread(target=server_sw,args=(s,))
    t.start()
