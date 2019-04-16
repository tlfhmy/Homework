from math import sqrt,atan2

class R2Vector(object):
    def __init__(self, x=0., y=0.):
        if type(x) == tuple or type(x) == list:
            self.x = float(x[0])
            self.y = float(x[1])
        else:
            self.x = float(x)
            self.y = float(y)
    
    def __add__(self, v):
        assert type(v) == R2Vector
        return R2Vector(self.x + v.x, self.y + v.y)
    
    def __iadd__(self, v):
        assert type(v) == R2Vector
        self.x += v.x
        self.y += v.y
        return self
    
    def __sub__(self, v):
        assert type(v) == R2Vector
        return R2Vector(self.x - v.x, self.y - v.y)
    
    def __isub__(self, v):
        assert type(v) == R2Vector
        self.x -= v.x
        self.y -= v.y
        return self
    
    def __mul__(self, v):
        if type(v) == R2Vector:
            return self.x*v.x + self.y*v.y
        else:
            return R2Vector(self.x*float(v), self.y*float(v))

    def __imul__(self, a):
        self.x *= float(a)
        self.y *= float(a)
        return self
    
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def __repr__(self):
        return "(" + repr(self.x) + "," + repr(self.y) + ")"
    
    def length(self):
        return sqrt(self.x*self.x + self.y*self.y)
    
    def normalized(self):
        l = self.length()
        if l > 0.:
            return R2Vector(self.x/l, self.y/l)
        else:
            return R2Vector(self.x, self.y)
    
    def normalize(self):
        l = self.length()
        if l > 0.:
            self.x /= l
            self.y /= l
        return self
    
    def normal(self):
        return R2Vector(-self.y, self.x)
    
    def angle(self, v):
        xx = v*self
        yy = v*self.normal()
        return atan2(yy, xx)
    
    def toR2Point(self):
        return R2Point(self.x, self.y)

    def toTuple(self):
        return (self.x, self.y)
    

class R2Point(object):

    def __init__(self, x=0., y=0.):
        if type(x) == tuple or type(x) == list:
            self.x = float(x[0])
            self.y = float(x[1])
        else:
            self.x = float(x)
            self.y = float(y)
    
    def __add__(self, v):
        assert type(v) == R2Point
        return R2Point(self.x + v.x, self.y + v.y)
    
    def __iadd__(self, v):
        assert type(v) == R2Point
        self.x += v.x
        self.y += v.y
        return self
    
    def __sub__(self, v):
        assert type(v) == R2Point
        return R2Point(self.x - v.x, self.y - v.y)
    
    def __isub__(self, v):
        assert type(v) == R2Point
        self.x -= v.x
        self.y -= v.y
        return self

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def __repr__(self):
        return "(" + repr(self.x) + "," + repr(self.y) + ")"
    
    def toVector(self):
        return R2Vector(self.x, self.y)
    
    def toTuple(self):
        return (self.x, self.y)


def intersectLines(p1, v1, p2, v2, esp=1e-8):
    n = v1.normal()
    s = n*v2
    if abs(s) <= esp:
        return (False, R2Point())
    t = n*(p1 - p2).toVector() / s
    p = p2.toVector() + v2*t

    return (True, p.toR2Point())
