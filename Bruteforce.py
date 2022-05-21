
from sympy import prime
import sympy


#all we've now is the value of n, test it.
#first, we must generate prime numbers, p & Q



def FindPQ(n):
    while True:
        primeList=[0,0]
        for i in range(0,2):
            x= sympy.randprime(2,2**8)
            primeList[i] = x
        
        if n == primeList[0]*primeList[1] :
            return primeList[0], primeList[1]
            

def GetP_Q():
      primeList=[0,0]
      while(primeList[0] == primeList[1]):
            for i in range(0, 2):
                  n = sympy.randprime(2, 2**8)
                  primeList[i] = n
      return primeList[0], primeList[1]

pOriginal,qOriginal = GetP_Q()

pFound,qFound = FindPQ(qOriginal * pOriginal)

print("P found = {pFound}")
print(qFound)
print("Q found = {qFound}")

     