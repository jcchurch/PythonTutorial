import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')
t.color('green', 'yellow')

t.down()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.up()
t.forward(150)

t.down()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

window.mainloop()
