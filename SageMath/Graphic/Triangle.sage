
#from math import sqrt,atan2

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




class Triangle(object):
    def __init__(self, pts=[]):
        assert type(pts) == list
        self.a = list(pts[0])
        self.b = list(pts[1])
        self.c = list(pts[2])
    
    def isTriangle(self):
        if (self.a)[0] + (self.b)[0] - (self.c)[0] < 1e-8 and\
            (self.a)[1] + (self.b)[1] - (self.c)[1] < 1e-8:
            return True
        else:
            return False
    
    def show(self):
        g = plot([])
        g += line([self.a, self.b])
        g += line([self.a, self.c])
        g += line([self.b, self.c])
        return(g)
    
    def Gen(self):
        ap = R2Point(self.a)
        bp = R2Point(self.b)
        cp = R2Point(self.c)

        ab = (bp - ap).toVector()
        ac = (cp - ap).toVector()
        ba = (ap - bp).toVector()
        bc = (cp - bp).toVector()

        pv1 = (ab.normalized() + ac.normalized()).normalized()
        pv2 = (ba.normalized() + bc.normalized()).normalized()

        o = ((intersectLines(ap, pv1, bp, pv2))[1])

        oa = (intersectLines(o, ab.normal(), ap, ab))[1]
        ob = (intersectLines(o, bc.normal(), bp, bc))[1]
        oc = (intersectLines(o, ac.normal(), cp, ac))[1]

        r = (oa - o).toVector().length()
        g = plot([])
        g += line([self.a, self.b])
        g += line([self.a, self.c])
        g += line([self.b, self.c])
        g += line([self.a, ob.toTuple()])
        g += line([self.b, oc.toTuple()])
        g += line([self.c, oa.toTuple()])
        g += circle(o.toTuple(),r,rgbcolor=(1,0,0))
        return g

