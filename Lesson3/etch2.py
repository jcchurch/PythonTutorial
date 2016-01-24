import turtle

t = turtle.Turtle()
t.shape('turtle')
t.color('green', 'green')

def up(): head(90)
def right(): head(0)
def left(): head(180)
def down(): head(270)

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

turtle.listen()
turtle.mainloop()
