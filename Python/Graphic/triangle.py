from tkinter import *
from R2Graph import *
from math import fabs

rootWindow = Tk()
rootWindow.title("Triangle")
rootWindow.geometry("800x600")
rootWindow.update()

points = []

drawArea = Canvas(
  rootWindow,
  width=800-8*2, height=600-8*2-24,
  bg="white"
)

drawArea.place(anchor="nw", x=8, y=8+24)

def onClear():
  points.clear()
  drawArea.delete("all")
  
clearButton = Button(
  text="Clear",
  width=60, height=20,
  command=onClear
)

clearButton.place(anchor="nw", x=8, y=8, width=60, height=20)

def onDraw():
  if len(points) < 3:
    return 
  drawArea.create_line(
    points[0],points[1],points[2], points[0],
    width=2, fill="blue"
  )
  
  t0 = R2Point(points[0])
  t1 = R2Point(points[1])
  t2 = R2Point(points[2])
  
  v01 = t1 - t0; v01.normalize()
  v02 = t2 - t0; v02.normalize()
  b0 = v01 + v02
  (_, p0) = intersectLines(
    t0, b0, t1, t2-t1
  )
  drawArea.create_line(
    (t0.x, t0.y), (p0.x, p0.y),
    fill="darkGreen", width=2
    )
  
  v12 = t2 - t1; v12.normalize()
  v10 = t0 - t1; v10.normalize()
  b1 = v12 + v10
  (_, p1) = intersectLines(
    t1, b1, t0, t2-t0
  )
  drawArea.create_line(
    (t1.x, t1.y), (p1.x, p1.y),
    fill="darkGreen", width=2
    )
  
  (_, c) = intersectLines(
    t0, b0, t1, b1
  )
  #r = (c - t0).length()
  n = (t2 - t0).normal()
  n.normalize()
  r = fabs((c - t0)*n)
  drawArea.create_oval(
    (c.x - r, c.y - r),
    (c.x + r, c.y + r),
    fill="", outline="red"
  )
  
  
  
drawButton = Button(
  text="Draw",
  width=60, height=20,
  command=onDraw
)

drawButton.place(anchor="nw", x=8 +60 + 8, y=8, width=60, height=20)

def onClick(e):
  points.append((e.x, e.y))
  drawArea.create_line(
    (e.x-8, e.y), (e.x+8, e.y),
    fill="red", width=3
  )
  drawArea.create_line(
    (e.x, e.y-8), (e.x, e.y+8),
    fill="red", width=3
  )
  
drawArea.bind("<Button-1>", onClick)

rootWindow.mainloop()
