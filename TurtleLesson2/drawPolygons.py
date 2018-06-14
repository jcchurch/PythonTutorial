import turtle
import random

window = turtle.Screen()

def drawPolygon(t, size, sides):
    t.down()
    for i in range(sides):
        t.forward(size / sides)
        t.left(360 / sides)

def makeTurtle(color1, color2):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(color1, color2)
    return t

def move(t, x, y):
    t.up()
    t.goto(x, y)

r = makeTurtle('red', 'red')
move(r, -300, -300)

for i in [3, 4, 5, 6, 8, 10, 100]:
    drawPolygon(r, 400, i)
    r.up()
    r.forward(120)

window.mainloop()
