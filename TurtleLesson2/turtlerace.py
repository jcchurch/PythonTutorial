import turtle
import random

window = turtle.Screen()

def makeTurtle(color1, color2):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(color1, color2)
    return t

def move(t, x, y):
    t.up()
    t.goto(x, y)

def moveForward(t):
    t.down()
    t.left(90)
    t.forward(random.randrange(100))
    t.right(90)
    t.forward(random.randrange(200))
    t.right(90)
    t.forward(random.randrange(100))
    t.left(90)
    t.forward(random.randrange(200))

r = makeTurtle('red', 'red')
l = makeTurtle('blue', 'blue')
m = makeTurtle('orange', 'orange')
d = makeTurtle('purple', 'purple')

move(r, -300, -300)
move(l, -300, -100)
move(m, -300, 100)
move(d, -300, 300)

for i in range(4):
    moveForward(r)
    moveForward(l)
    moveForward(m)
    moveForward(d)

window.mainloop()
