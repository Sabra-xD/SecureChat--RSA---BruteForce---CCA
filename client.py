import threading
import socket
from RSA2 import *


p, q = GetP_Q()
n = p  * q
phi_n = (p-1)* (q-1)
e = Calculate_e(phi_n)

#M = to_Asci(m)
#m_weight = max(M)

def findweight(M):
    m_weight = max(to_Asci(M))
    while(m_weight > n):
       p, q = GetP_Q()
       n = p  * q
       phi_n = (p-1)* (q-1)
       e = Calculate_e(phi_n)

d = mult_inv(e, phi_n)

print(n)
print(p)
print(q)
















alias = input('Choose an alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 49000))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
               M = Decryption(message,d,n)
               print(M)
               
                
                
        
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        #findweight(input(""))
        C = Encryption(input(""),e,n)
        ActualMessage = f'{alias} : {C}'
        client.send(ActualMessage.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
