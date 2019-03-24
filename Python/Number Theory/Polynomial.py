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
        elif type(x) == int:
            assert(x >= 0)
            tmp = []
            for i in range(0, x+1):
                tmp.append(RaNum(0,1))
            tmp[-1] = RaNum(1,1)
            self.x = tmp
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
        tmp = self + (-v)
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
            keeps = [RaNum()] * (2*(len(self.x)+len(v.x)))
            keepv = deepcopy(keeps)
            tmp = [RaNum()] * (len(self.x)+len(v.x))
            for i in range(0,len(self.x)):
                keeps[i] = (self.x)[i]
            for i in range(0,len(v.x)):
                keepv[i] = (v.x)[i]
            for i in range(0,(len(self.x)+len(v.x))):
                val = RaNum()
                for j in range(0,i+1):
                    val += keeps[j]*keepv[i-j]
                tmp[i] = val
            tmppol = Polynomial(tmp)
            tmppol.Recom()
            return tmppol
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
            return self
        else:
            t1 = deepcopy(self)
            t2 = deepcopy(v)
            n = int(len(self.x) - len(v.x))
            t2 *= Polynomial(n)
            fac = (t1.x)[-1] / (t2.x)[-1]
            cong = t1 - t2*fac
            if (len(cong.x) >= len(v.x)) and (len(cong.x) != 1):
                cong = cong % v
            return cong 

    def __floordiv__(self, v):
        assert type(v) == Polynomial
        assert not(v.zeropoly())
        if len(self.x) < len(v.x):
            return Polynomial([RaNum()])
        else:
            t1 = deepcopy(self)
            t2 = deepcopy(v)
            n = int(len(self.x) - len(v.x))
            t2 *= Polynomial(n)
            fac = (t1.x)[-1] / (t2.x)[-1]
            fact = Polynomial(n)*fac

            cong = t1 - t2*fac
            if (len(cong.x) >= len(v.x)) and (len(cong.x) != 1):
                fact += (cong // v)
            return fact

    def __eq__(self, v):
        assert type(v) == Polynomial
        self.Recom()
        v.Recom()
        return self.x == v.x

    def zeropoly(self):
        if (len(self.x) == 1) and ((self.x)[0]).iszero():
            return True
        else:
            return False

    def Recom(self):
        if (self.x)[-1].iszero() and (len(self.x) > 1):
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

def polygcd(a, b):
    assert type(a) == Polynomial and type(b) == Polynomial
    if len(a.x) >= len(b.x):
        tmax = deepcopy(a)
        tmin = deepcopy(b)
    else:
        tmax = deepcopy(b)
        tmin = deepcopy(a)
    if (tmax % tmin) == Polynomial([RaNum()]):
        return tmin
    else:
        return polygcd(tmin, tmax % tmin)
