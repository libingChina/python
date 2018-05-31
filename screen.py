from PIL import ImageGrab
import socket
import time
a=time.time()
img=ImageGrab.grab()
img.save('123.jpeg')
f=open('123.jpeg','rb')
udp= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
udp.bind(('',8888))
while True:
    f1=f.read(1024)
    if f1:
        udp.sendto(f1,('192.168.199.255',8889))
    else:
        udp.sendto(''.encode(), ('192.168.199.255', 8889))
        break
udp.close()
print(time.time()-a)