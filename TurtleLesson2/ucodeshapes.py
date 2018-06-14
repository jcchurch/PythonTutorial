import turtle

def drawSquare(t, size):
    t.down()
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)

def moveUnderSquare(t):
    t.up()
    t.right(90)
    t.forward(110)
    t.left(90)

window = turtle.Screen()

def makeTurtle(color1, color2):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(color1, color2)
    return t

t = makeTurtle('green', 'yellow')

r = turtle.Turtle()
r.shape('turtle')
r.color('red', 'red')

drawSquare(t, 100)
moveUnderSquare(t)
drawSquare(t, 100)

r.up()
r.forward(150)

for i in range(4):
    drawSquare(r, 80)
    moveUnderSquare(r)

window.mainloop()

