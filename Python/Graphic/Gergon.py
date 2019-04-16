from tkinter import *
from R2Vector import *

#def create_circle(p, r):
    #assert type(p) == R2Point
    

win = Tk()
win.title("Gen")
win.geometry("800x600")

points = []

winx = 0
winy = 0

drawArea = Canvas(
    win,
    width=800-8*2, height=600-8*2-24,
    bg="white"
)

drawArea.place(anchor="nw", x=8, y=8+24)

def onClear():
    points.clear()
    drawArea.delete("all")

ClearButton = Button(
    text="Clear",
    width=60, height=20,
    command = onClear
)

ClearButton.place(anchor="nw", x=8, y=8, width=60, height=20)

def onDraw():
    if len(points) < 3:
        return
    drawArea.create_line(
        points[0], points[1], points[2], points[0],
        width=2, fill="green"
    )

    ap = R2Point(points[0])
    bp = R2Point(points[1])
    cp = R2Point(points[2])

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

    drawArea.create_line(
        points[0],ob.toTuple(),
        width=2, fill="green"
    )
    drawArea.create_line(
        points[1],oc.toTuple(),
        width=2, fill="green"
    )
    drawArea.create_line(
        points[2],oa.toTuple(),
        width=2, fill="green"
    )

    drawArea.create_oval(
        o.x-r, o.y-r, o.x+r, o.y+r,
        width=2,outline="red"
    )

drawButton = Button(
    text="Draw",
    width=60, height=20,
    command = onDraw
)

drawButton.place(anchor="nw", x=60+8+2, y=8, width=60, height=20)

def onClick(e):
    if len(points) < 3:
        points.append((e.x, e.y))
        drawArea.create_line(
            (e.x-8, e.y), (e.x+8, e.y),
            fill="red", width=3
        )
        drawArea.create_line(
            (e.x, e.y-8), (e.x, e.y+8),
            fill="red", width=3
        )

drawArea.bind("<Button-1>",onClick)

def sizeChanged(event):
    winx = win.winfo_width() - 2*8
    winy = win.winfo_height()- 2*8 - 24
    drawArea.config(width=winx, height=winy)
    drawArea.place(anchor="nw", x=8, y=8+24)
win.bind("<Configure>", sizeChanged)

win.mainloop()