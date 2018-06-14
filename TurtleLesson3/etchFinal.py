import turtle

t = turtle.Turtle()
t.shape('turtle')
t.color('green', 'green')

def up(): head(90)
def right(): head(0)
def left(): head(180)
def down(): head(270)
def yellow(): t.pencolor('yellow')
def green(): t.pencolor('green')
def red(): t.pencolor('red')
def blue(): t.pencolor('blue')

def square():
    t.down()
    for i in range(4):
        t.forward(100)
        t.left(90)

def triangle():
    t.down()
    for i in range(3):
        t.forward(100)
        t.left(120)

def circle():
    t.down()
    t.circle(50)

def head(x):
    t.seth(x)
    t.forward(2)

def flipTail():
    if t.isdown():
        t.up()
    else:
        t.down()

turtle.onkey(up, 'Up')
turtle.onkey(right, 'Right')
turtle.onkey(left, 'Left')
turtle.onkey(down, 'Down')
turtle.onkey(flipTail, 'space')
turtle.onkey(yellow, 'y')
turtle.onkey(red, 'r')
turtle.onkey(blue, 'b')
turtle.onkey(green, 'g')
turtle.onkey(square, 's')
turtle.onkey(triangle, 't')
turtle.onkey(circle, 'c')

turtle.listen()
turtle.mainloop()
