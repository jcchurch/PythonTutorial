import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')
t.color('green', 'yellow')

# Draw the building
t.down()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# Move to start of the roof.
t.left(90)
t.forward(100)
t.right(90)

# Draw the roof.
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

# Move to door
t.right(90)
t.forward(100)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.right(90)
t.forward(20)
t.right(90)
t.forward(40)

window.mainloop()
