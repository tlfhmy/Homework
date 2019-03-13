from NumTheFunc import gcd

class RaNum(object):


    def __init__(self, x=0, y=1):
        if type(x) != int or type(y) != int:
            print("Please enter integer!")
            return
        else:
            if y == 0:
                print("Denominator can not be 0!")
                return
            else:
                self.x = int(x)
                self.y = int(y)
                self.simplify()

    def simplify(self):
        if self.x * self.y > 0:
            self.x = abs(self.x)
            self.y = abs(self.y)
        elif self.x * self.y == 0:
            self.x = 0
            self.y = 1
        else:
            self.x = -abs(self.x)
            self.y = abs(self.y)
        
        c = gcd(self.x, self.y)
        if c != 1:
            self.x = self.x // c
            self.y = self.y // c

    def __add__(self, b):
        assert type(b) == RaNum
        ta = self.x; tb = self.y
        ta *= b.y; tb *= b.y
        ta += b.x * self.y
        tmp = RaNum(ta,tb)
        tmp.simplify()
        return tmp

    def __iadd__(self, b):
        assert type(b) == RaNum
        self = self + b
        self.simplify()
        return self
    
    def __mul__(self, b):
        assert type(b) == RaNum
        ta = self.x; tb = self.y
        ta *= b.x; tb *= b.y
        tmp = RaNum(ta,tb)
        tmp.simplify()
        return tmp
    
    def __imul__(self, b):
        assert type(b) == RaNum
        self = self * b
        self.simplify()
        return self
    
    def recip(self):
        assert self.x != 0
        tmp = RaNum(self.y,self.x)
        tmp.simplify()
        return tmp
    
    def __truediv__(self, b):
        assert type(b) == RaNum
        tmp = self * b.recip()
        tmp.simplify()
        return tmp
    
    def __itruediv__(self, b):
        assert type(b) == RaNum
        self = self / b
        self.simplify()
        return self
    
    def __neg__(self):
        tmp = RaNum(-self.x, self.y)
        tmp.simplify()
        return tmp
    
    def __sub__(self, b):
        tmp = self + (-b)
        tmp.simplify()
        return tmp
    
    def __isub__(self, b):
        assert type(b) == RaNum
        self = self - b
        self.simplify()
        return self

    def __int__(self):
        return self.x // self.y
    
    def __float__(self):
        return self.x / self.y

    def __str__(self):
        return str(self.x) + "/" + str(self.y)

    def __repr__(self):
         return repr(self.x) + "/" + repr(self.y)
    
    def iszero(self):
        return self.x == 0