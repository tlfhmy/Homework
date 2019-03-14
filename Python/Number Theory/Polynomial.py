from RaNum import *
from copy import deepcopy

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
        tmp = Polynomial(temp)
        tmp.Recom()
        return tmp

    def __iadd__(self, v):
        assert type(v) == Polynomial
        self = self + v
        self.Recom()
        return self

    def __neg__(self):
        tmp = deepcopy(self)
        for i in range(0, len(tmp.x)):
            (tmp.x)[i] = -(tmp.x)[i]
        tmp.Recom()
        return tmp
    
    def __sub__(self, v):
        assert type(v) == Polynomial
        tmp = -v + self
        tmp.Recom()
        return tmp

    def __isub__(self, v):
        assert type(v) == Polynomial
        tmp = -deepcopy(self)
        self = tmp + v
        self.Recom()
        return self

    def __mul__(self, v):
        assert (type(v) == Polynomial) or (type(v) == RaNum)
        if type(v) == Polynomial:
            tf = [RaNum(0,1)] * max(len(self.x), len(v.x))
            tg = deepcopy(tf)
            th = deepcopy(tf)
            for i in range(0,len(self.x)):
                tf[i] = (self.x)[i]
            for i in range(0, len(v.x)):
                tg[i] = (v.x)[i]
            for i in range(0, len(tf)):
                for j in range(0, i):
                    th[i] += tf[j] * tg[i-j]
            tmp = Polynomial(th)
            tmp.Recom()
            return tmp
        else:
            tmp = deepcopy(self)
            for i in range(0,len(tmp.x)):
                (tmp.x)[i] *= v
            return tmp

    def __imul__(self, v):
        assert type(v) == Polynomial
        self = self * v
        return self

    def __mod__(self, v):
        assert type(v) == Polynomial
        assert not(v.zeropoly())
        if len(self.x) < len(v.x):
            tmax = deepcopy(v)
            tmin = deepcopy(self)
        else:
            tmax = deepcopy(self)
            tmin = deepcopy(v)
        tmax.Recom()
        tmin.Recom()
        tp = deepcopy(tmin)
        n = len(tmax.x) - len(tmin.x)
        while n != 0:
            tmin.x.insert(0,RaNum(0,1))
            n -= 1
        fac = (tmax.x)[-1] / (tmin.x)[-1]
        tmax = tmax - tmin * fac
        tmax.Recom()
        if len(tmax.x) >= len(tp.x):
            tmax = tmax % tp
        return tmax
    
    def zeropoly(self):
        if (len(self.x) == 1) and ((self.x)[0]).iszero():
            return True
        else:
            return False

    def Recom(self):
        if (self.x)[-1].iszero():
            del (self.x)[-1]
            self.Recom()
        return

    def __str__(self):
        strs = ""
        for i in range(0,len(self.x)-1):
            if not(((self.x)[i]).iszero()):
                if i == 0:
                    strs += str((self.x)[i]) + " + "
                else:
                    strs += str((self.x)[i]) + "x^" + str(i) + " + "
        if len(self.x) != 1:
            strs += str((self.x)[len(self.x)-1]) + "x^" + str(len(self.x)-1)
        else:
            strs += str((self.x)[len(self.x)-1])
        return strs

    def __repr__(self):
        return str(self)