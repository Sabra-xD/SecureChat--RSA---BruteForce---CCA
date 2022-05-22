import threading
import socket

from ast import Continue
import sympy
import random


global poriginal,qoriginal
condition = False
Choice = int(input(" Input 1 for Auto Key Generation - Input 0 for manuale input of P & Q"))
if Choice == 0 :
      while True:
       poriginal = int(input("Enter the Value of P:  "))
       qoriginal = int(input("Enter the value of Q:  "))
       if(sympy.isprime(qoriginal) and sympy.isprime(poriginal)):
             condition = True
             break


def GetP_Q(): 
      primeList=[0,0]
      while(primeList[0] == primeList[1]):
            for i in range(0, 2):
                  n = sympy.randprime(2, 2**8)
                  primeList[i] = n
            return primeList[0], primeList[1]

def GCD(x, y):
    if(y == 0):
        return x
    else:
        return GCD(y, x%y)
#get E
def Calculate_e(phi_n):
      e = 2
      while(e < phi_n):
            if GCD(e,phi_n) == 1:
                  return e   
            else:
                  e = e +1

#Convert Message to Asci code 
def to_Asci(M):
      ascii_values = []
      for character in M:
            ascii_values.append(ord(character))
      
      return ascii_values

def str_to_int(M):
      return [int(i) for i in M]
def List_to_Str(list_array):
      return ' '.join([str(l)for l in list_array])

def str_to_list(str):
      return list(str.split(" "))
#RSA Encryption
def Encryption(M, e, n ):
      C =[]
      MessageList = to_Asci(M)
      

      for m in MessageList:
            C.append((m ** e) % n)
      return C
#Extended Euclidean Algorithm
def ExtendedEuclid(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = ExtendedEuclid(b,a%b)
        s = s-((a//b) * t)
        return(gcd,t,s)

#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=ExtendedEuclid(e,r)
    if(gcd!=1):
        return None
    else:
        return s%r

#RSA Decryption
def Decryption(C, d, n):
      M = []
      for c in C:
            M.append((c ** d) % n)      
      
      return M
def toStr(asci):
      return (''.join(chr(i) for i in asci))


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
                  if message.find('Keys:')!= -1:
                        temp = message.find('Keys:')
                        PU = str_to_list(message[temp:])
                        e = int(PU[1])
                        n = int(PU[2])
                        phi_n = int(PU[3])
                        user_name = message[0]
                        M = str_to_list(message)
                        user_name = M[0]
                        for i in range(0, 3):    
                              if(i == 0):
                                    M.pop(-1)
                                    M.pop(0)
                              M.pop(-1)
                        
                        M = str_to_int(M)
                        #print(M)
                        d = mult_inv(e, phi_n)
                        M = Decryption(M, d, n)
                        #print("user name is "+ user_name)
                        print(user_name+toStr(M))
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        x = f'{alias}: '
        message = f'{input("")}'      
        p, q = GetP_Q()
        while Choice == 0:
              p=poriginal
              q= qoriginal
              break
        n = p  * q
        print(p)
        print(q)
        phi_n = (p-1)* (q-1)

        e = Calculate_e(phi_n)
        M = to_Asci(message)
        m_weight = max(M)
        while m_weight > n :
            p,q=GetP_Q()
            n = p  * q
            phi_n = (p-1)* (q-1)
            e = Calculate_e(phi_n)
        cipher = Encryption(message, e, n)
        stringCipher = List_to_Str(cipher)
        PU = [' Keys:', str(e), str(n), str(phi_n)]
        PU_str = List_to_Str(PU)
        client.send((x + stringCipher + PU_str ).encode('utf-8'))
        
        

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()