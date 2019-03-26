from RaNum import *
from Polynomial import *


a = [RaNum(4,5),RaNum(0,1),RaNum(-3,7),RaNum(0,1),RaNum(3,4)]
b = [RaNum(1,7),RaNum(1,6)]

#a = [RaNum(1,7),RaNum(1,6)]
#b = [RaNum(1,1)]

fa = Polynomial(a)
fb = Polynomial(b)

print(fa)
print(fb)
print("fa+fb",fa+fb)
print("fa-fb",fa-fb)
print("fa*fb",fa*fb)
print("fa%fa",fa%fb)
print("fa//fb",fa//fb)

#print(fa % fb)
#print(fa // fb)
#print(Polynomial(0))

#print(fa * fb)

print("polygcd(fa,fb)",polygcd(fa,fb))