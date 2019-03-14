from RaNum import *
from Polynomial import *


a = [RaNum(4,5),RaNum(0,1),RaNum(-3,7),RaNum(0,1),RaNum(3,4)]
b = [RaNum(1,7),RaNum(1,6)]

fa = Polynomial(a)
fb = Polynomial(b)

print(fa)
print(fb)

print(fa % fb)