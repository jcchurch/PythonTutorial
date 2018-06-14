import turtle

def makeTurtle(color1, color2):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(color1, color2)
    return t

window = turtle.Screen()
t = makeTurtle('green', 'yellow')

for i in range(4):
    t.circle(40)
    t.forward(100)

window.mainloop()
