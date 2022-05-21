from ast import Continue
import sympy
import random
def GetP_Q():
      primeList=[0,0]
      while(primeList[0] == primeList[1]):
            for i in range(0, 2):
                  n = sympy.randprime(2, 2**8)
                  primeList[i] = n
      return primeList[0], primeList[1]
      #return 17,11

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
      print("entered teh decryption")
      
      for c in C:
            print("Inside the loop")
            print('This is M so far {M}')
            M[c] = (c**d) % n
            print("Never made it psat here?")   
      print("Should fucking return here!")
      return M



def toStr(asci):
      return (''.join(chr(i) for i in asci))

