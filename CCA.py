from xml.etree.ElementTree import tostring
from sympy import Q
from RSA2 import *





def FindR(n):
    while True:
     r = random.randint(2,2**8)
     if( n % r == 1):
         return r




def Decryption2(C,r,n):
      M = []
      for c in C:
            x= mult_inv(r,n)
            M.append(c * x % n)
      return M





def Encryption2(Cs,r,e,n):
      C =[]
      MessageList = to_Asci(Cs)
      for m in MessageList:
            C.append((m *  (r**e)) % n)
      return C




p, q = GetP_Q()
n = p*q
phi_n = (p-1) * (q-1)
# we need to get e here.
e = Calculate_e(phi_n)
d = mult_inv(e,phi_n)
#print(e)
#print(d)


M = input("Enter Message: ")



r = FindR(n)

#print(r)
C = Encryption(M,e,n)

C_sharp = Encryption2(toStr(C),r,e,n)

Y = Decryption(C_sharp,d,n)

M2= Decryption2(Y,r,n)
print(toStr(M2))


