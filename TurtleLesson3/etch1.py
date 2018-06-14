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

turtle.onkey(up, 'Up')
turtle.onkey(right, 'Right')
turtle.onkey(left, 'Left')
turtle.onkey(down, 'Down')

turtle.listen()
turtle.mainloop()
