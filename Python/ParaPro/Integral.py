from threading import Thread
from time import sleep
import tkinter as tk
from tkinter import Canvas
from math import sin,cos,pi,exp,sqrt

xmin = -sqrt(pi)
xmax = sqrt(pi)

def function(x):
    return exp(-x**2)

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

win = tk.Tk()
win.title("Integral")
win.geometry("800x600")
win.resizable(0,0)


drawArea = Canvas(
    win,
    width = 800- 8*2, height = 600-8*2-24,
    bg = "white"
)

drawArea.place(anchor="nw", x=8, y=24+8)

drawArea.create_line(
    (400-8,0), (400-8,520),
    fill="black",width = 2
)
drawArea.create_line(
    (0,260), (800-2*8, 260),
    fill="black", width=2
)
drawArea.create_line(
    (0,520), (800-2*8, 520),
    fill="black", width=2
)

aLable = tk.Label(
    text = "Integral:",
    width = 10, height = 1
)
lValue = tk.Label(
    text = "0.0",
    width = 10, height = 1
)
aLable.place(anchor="nw", x = 350, y = 560)
lValue.place(anchor="nw", x = 430, y = 560)

def create_coord(x1,y1,x2,y2):
    drawArea.create_line(
        (x1+15, (y1+y2)/2), (x2-15, (y1+y2)/2),
        fill="black", width=1
    )
    drawArea.create_line(
        (x2-15, (y1+y2)/2), (x2-15-5, (y1+y2)/2 - 5),
        fill = "black", width=1
    )
    drawArea.create_line(
        (x2-15, (y1+y2)/2), (x2-15-5, (y1+y2)/2 + 5),
        fill = "black", width=1
    )
    drawArea.create_line(
        ((x1+x2)/2, y2-8), ((x1+x2)/2, y1+8),
        fill = "black", width=1
    )
    drawArea.create_line(
        ((x1+x2)/2, y1+8), ((x1+x2)/2 - 5, y1+8 + 5),
        fill="black", width=1
    )
    drawArea.create_line(
        ((x1+x2)/2, y1+8), ((x1+x2)/2 + 5, y1+8 + 5),
        fill="black", width=1
    )

create_coord(0,0,392,260)
create_coord(392,0,784,260)
create_coord(0,260,392,520)
create_coord(392,260,784,520)


points = []
<<<<<<< HEAD
N = 1000
wait_time = 0.01

def dwait(wt):
    if wt < 1e-8:
        return
    else:
        sleep(wt)

=======
N = 5000
>>>>>>> 7295f27573a95f88af51d7920046cbd1d0ee6a2d
for i in range(0,N):
    xi = xmin+(xmax - xmin)/N*i
    yi = function(xi)
    points.append((xi, yi))

integral = 0.0


x_coordgap = (xmax - xmin) / 20.
y_coordgap = (ymax - ymin) / 20.

x1 = xmin - x_coordgap
x2 = xmax + x_coordgap
y1 = ymin - y_coordgap
y2 = ymax + y_coordgap

def part1():
    tpx = trancor(x1,x2,15,392-15)
    tpy = trancor(y1,y2,260-5,5)
    for i in range(0,N//4):
        if i < N-1:
            drawArea.create_line(
                (tpx[0]*points[i][0]+tpx[1], tpy[0]*points[i][1] + tpy[1]),
                (tpx[0]*points[i+1][0]+tpx[1], tpy[0]*points[i+1][1] + tpy[1]),
                fill = "red", width = 1
            )
           
    for i in range(0,N//4):
        if i < N-1:
            global integral
            integral += (xmax-xmin)/N*points[i][1]
            drawArea.create_rectangle(
                tpx[0]*points[i][0]+tpx[1], tpy[0]*points[i][1] + tpy[1],
                tpx[0]*points[i+1][0]+tpx[1], tpy[0]*0 + tpy[1],
                fill="green", width=0
            )
            dwait(wait_time)
            lValue.configure(text=str(integral)[0:7])

def part2():
    tpx = trancor(x1,x2,392+15,784-15)
    tpy = trancor(y1,y2,260-5,5)
    for i in range(N//4,N//2):
        if i < N-1:
            drawArea.create_line(
                (tpx[0]*points[i][0]+tpx[1], tpy[0]*points[i][1] + tpy[1]),
                (tpx[0]*points[i+1][0]+tpx[1], tpy[0]*points[i+1][1] + tpy[1]),
                fill = "red", width = 1
            )
            
    for i in range(N//4,N//2):
        if i < N-1:
            global integral
            integral += (xmax-xmin)/N*points[i][1]
            drawArea.create_rectangle(
                tpx[0]*points[i][0]+tpx[1], tpy[0]*points[i][1] + tpy[1],
                tpx[0]*points[i+1][0]+tpx[1], tpy[0]*0 + tpy[1],
                fill="green", width=0
            )
            dwait(wait_time*2)
            lValue.configure(text=str(integral)[0:7])

def part3():
    tpx = trancor(x1,x2,15,392-15)
    tpy = trancor(y1,y2,520-5,260+5)
    for i in range(N//2,N*3//4):
        if i < N-1:
            drawArea.create_line(
                (tpx[0]*points[i][0]+tpx[1], tpy[0]*points[i][1] + tpy[1]),
                (tpx[0]*points[i+1][0]+tpx[1], tpy[0]*points[i+1][1] + tpy[1]),
                fill = "red", width = 1
            )
            
    for i in range(N//2,N*3//4):
        if i < N-1:
            global integral
            integral += (xmax-xmin)/N*points[i][1]
            drawArea.create_rectangle(
                tpx[0]*points[i][0]+tpx[1], tpy[0]*points[i][1] + tpy[1],
                tpx[0]*points[i+1][0]+tpx[1], tpy[0]*0 + tpy[1],
                fill="green", width=0
            )
            dwait(wait_time*4)
            lValue.configure(text=str(integral)[0:7])

def part4():
    tpx = trancor(x1,x2,392+15,784-15)
    tpy = trancor(y1,y2,520-5,260 + 5)
    for i in range(N*3//4,N):
        if i < N-1:
            drawArea.create_line(
                (tpx[0]*points[i][0]+tpx[1], tpy[0]*points[i][1] + tpy[1]),
                (tpx[0]*points[i+1][0]+tpx[1], tpy[0]*points[i+1][1] + tpy[1]),
                fill = "red", width = 1
            )
            
    for i in range(N*3//4,N):
        if i < N-1:
            global integral
            integral += (xmax-xmin)/N*points[i][1]
            drawArea.create_rectangle(
                tpx[0]*points[i][0]+tpx[1], tpy[0]*points[i][1] + tpy[1],
                tpx[0]*points[i+1][0]+tpx[1], tpy[0]*0 + tpy[1],
                fill="green", width=0
            )
            dwait(wait_time*8)
            lValue.configure(text=str(integral)[0:7])

t1 = Thread(target=part1)
t2 = Thread(target=part2)
t3 = Thread(target=part3)
t4 = Thread(target=part4)

t1.start()
t2.start()
t3.start()
t4.start()

win.mainloop()
