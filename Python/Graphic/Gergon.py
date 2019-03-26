from tkinter import *
from R2Graph import *


win = Tk()
win.title("Gen")
win.geometry("800x600")

points = []

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



win.mainloop()