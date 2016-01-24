import turtle

def makeTurtle(color1, color2):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(color1, color2)
    return t

window = turtle.Screen()
t = makeTurtle('green', 'yellow')

numberOfCircles = int(input('How many circles?   '))

for i in range(numberOfCircles):
    t.circle(40)
    t.forward(100)

window.mainloop()
