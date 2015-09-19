import turtle

window = turtle.Screen()

george = turtle.Turtle()
george.shape('turtle')
george.color('green', 'yellow')

george.down()
george.begin_fill()
george.forward(100)

george.end_fill()

window.mainloop()
