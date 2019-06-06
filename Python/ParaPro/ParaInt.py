from threading import Thread
from time import sleep
from math import sin,cos,pi,exp,sqrt,log

xmin = -5
xmax = 5

def function(x):
    return exp(-x**2/2+4*x)

def find_range():
    ymin = function(xmin)
    ymax = function(xmin)
    step = (xmax - xmin) / 5000
    for i in range(0,5000):
        fva = function(xmin + i*step)
        if fva <= ymin:
            ymin = fva
        if fva >= ymax:
            ymax = fva
    return max(abs(ymin), abs(ymax))


ymax = find_range()
ymin = -ymax

def trancor(a,b,c,d):
    return ((c-d)/(a-b), (a*d-b*c)/(a-b))


points = []
N = 1000
wait_time = 0.01

def dwait(wt):
    if wt < 1e-8:
        return
    else:
        sleep(wt)

for i in range(0,N):
    xi = xmin+(xmax - xmin)/N*i
    yi = function(xi)
    points.append((xi, yi))

integral = 0.0


x_coordgap = (xmax - xmin) / 20.
y_coordgap = (ymax - ymin) / 20.


def part1():
    for i in range(0,N//4):
        if i < N-2:
            global integral
            integral += (xmax-xmin)/N*points[i][1]
            print("Part1")

def part2():
    for i in range(N//4,N//2):
        if i < N-2:
            global integral
            integral += (xmax-xmin)/N*points[i][1]
            print("Part2")

def part3():      
    for i in range(N//2,N*3//4):
        if i < N-2:
            global integral
            integral += (xmax-xmin)/N*points[i][1]
            print("Part3")

def part4():   
    for i in range(N*3//4,N):
        if i < N-2:
            global integral
            integral += (xmax-xmin)/N*points[i][1]
            print("Part4")

t1 = Thread(target=part1)
t2 = Thread(target=part2)
t3 = Thread(target=part3)
t4 = Thread(target=part4)

t1.start()
t2.start()
t3.start()
t4.start()

print(integral)