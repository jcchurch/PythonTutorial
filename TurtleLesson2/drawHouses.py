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

def drawTriangle(t, size):
    t.down()
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)

window = turtle.Screen()

def makeTurtle(color1, color2):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(color1, color2)
    return t

t = makeTurtle('green', 'yellow')
r = makeTurtle('red', 'red')

drawSquare(t, 100)

r.up()
r.left(90)
r.forward(100)
r.right(90)

drawTriangle(r, 100)

t.up()
t.forward(150)

r.up()
r.forward(150)

drawSquare(t, 100)
drawTriangle(r, 100)

t.up()
t.forward(150)

r.up()
r.forward(150)

drawSquare(t, 100)
drawTriangle(r, 100)

window.mainloop()
