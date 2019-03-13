from RaNum import *

class Polynomial(object):

    def __init__(self, x):
        if type(x) == tuple or type(x) == list:
            for i in x:
                if type(i) != RaNum:
                    print("All elements should be Rational Number!")
                    return
            self.x = list(x)
        else:
            print("Must use tuple or list type to initial Polynomial.")
            return
    
    def __add__(self, v):
        assert type(v) == Polynomial
        p = max(len(self.x), len(v.x))
        temp = [RaNum(0,1)] * p
        if len(self.x) > len(v.x):
            for i in range(0,len(v.x)):
                temp[i] = (self.x)[i] + (v.x)[i]
            for i in range(len(v.x),len(self.x)):
                temp[i] = (self.x)[i]
        else:
            for i in range(0,len(self.x)):
                temp[i] = (self.x)[i] + (v.x)[i]
            for i in range(len(v.x),len(self.x)):
                temp[i] = (v.x)[i]
        return Polynomial(temp)

    def __str__(self):
        strs = ""
        for i in range(0,len(self.x)-1):
            if not(((self.x)[i]).iszero()):
                strs += str((self.x)[i]) + "x^" + str(i) + " + "
        strs += str((self.x)[len(self.x)-1]) + "x^" + str(len(self.x)-1)
        return strs
    def __repr__(self):
        return str(self)