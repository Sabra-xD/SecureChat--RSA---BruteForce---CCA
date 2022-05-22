
from random import random
from sympy import prime
from matplotlib import pyplot as plt


from Crypto.Util import number

import time
import sympy
import random



#all we've now is the value of n, test it.
#first, we must generate prime numbers, p & Q







def FindPQ(n,no_bits):
    start = time.perf_counter()
    while True:
        primeList=[0,0]
        for i in range(0,2):
            x = random.randint(no_bits/2)
            
            primeList[i] = x
        
        if n == primeList[0]*primeList[1] :
            end = time.perf_counter()
            return end-start
            
            



def GetP_Q(no_bits):
      primeList=[0,0]
      while(primeList[0] == primeList[1]):
            for i in range(0, 2):
                  n = sympy.randprime(no_bits/2)
                  primeList[i] = n
      return primeList[0], primeList[1]









Time = []
x= []
y = []
for i in range(6,64) :
    p,q = GetP_Q(i)
    n = p * q
    print(n)
    x.append(n)
    Time = FindPQ(n,i)
    print(Time)
    y.append(Time)

 


plt.plot(x,y)
plt.show()