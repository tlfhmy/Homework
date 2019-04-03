from tkinter import *

win = Tk()
win.title("Bezier Curve")
win.geometry("800x600")


def Fac(n):
    tp = 1
    for i in range(1, n+1):
        tp *= i
    return tp

def C(m, n):
    return Fac(n) // (Fac(m) * Fac(n - m))


points_click = []
points_curve = []

drawArea = Canvas(
    win,
    width = 800-8*2, height=600-8*2-24,
    bg="white"
)
drawArea.place(anchor="nw", x=8, y=8+24)

def onClear():
    points_click.clear()
    points_curve.clear()
    drawArea.delete("all")

clearButton = Button(
    text="Clear",
    width=60, height=20,
    command=onClear
)

clearButton.place(anchor="nw", x=8, y=8, width=60, height=20)

def onDraw():
    points_curve.clear()
    #drawArea.delete("all")
    def f(n, t, pnt):
        tp = [0.0, 0.0]
        for i in range(0, n):
            tp[0] += C(i, n-1)*pow(1-t,n-i-1)*pow(t,i)*(pnt[i][0])
            tp[1] += C(i, n-1)*pow(1-t,n-i-1)*pow(t,i)*(pnt[i][1])
        return (tp[0], tp[1])
    

    for i in range(0, 1000):
        points_curve.append(f(len(points_click), i/999, points_click))
    
    drawArea.create_line(points_curve, fill="green", width=2)


drawButton = Button(
    text="Draw",
    width=60, height=20,
    command=onDraw
)

drawButton.place(anchor="nw", x=8+60+8, y=8, width=60, height=20)

def onClick(e):
    points_click.append((e.x, e.y))
    drawArea.create_line(
        (e.x-8, e.y), (e.x+8, e.y),
        fill="red", width=2
    )
    drawArea.create_line(
        (e.x, e.y-8), (e.x, e.y+8),
        fill="red", width=2
    )

drawArea.bind("<Button-1>", onClick)

win.mainloop()