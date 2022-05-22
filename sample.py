
from RSA2 import *
msg= """You see me, I come from the roads
You wanna try and put Skepta on hold
But no, badboy I've been one of those
Wake up call, you will get one of those
One to the eyeball, one to the nose
I don't really care about your postcode"""

p,q = GetP_Q()
print("p= ",p)
print("q= ",q)

n = p*q
print("n= ",n)

phi = (p-1)*(q-1)
print("phi= ",phi)

e = Calculate_e(phi)
print("e= ",e)

C = Encryption(msg,e,n)
print(C)

d = mult_inv(e,phi)
print(d)