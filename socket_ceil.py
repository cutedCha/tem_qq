import socket
import threading
BUFSIZE=1024
ip_port=('127.0.0.1',8080)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
res=s.connect_ex(ip_port)
class get_ms() :
    def main(self):
        while True :
            mess = s.recv(1000).decode('utf-8')
            print(mess)
    def __init__(self):
        self.main()
t = threading.Thread(target=get_ms,args=())
t.start()
while True:
    msg=input('>>: ').strip()
    s.send(msg.encode('utf-8'))

